from io import BytesIO
from multiprocessing import Pool
from typing import Dict, Iterable, Optional, Sequence, Tuple, Union
import matplotlib as mpl
import numpy as np
from matplotlib.colors import to_rgb
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde, probplot
from tqdm import tqdm
from .multivariate import MultiVariable
from .validate import (
    validate_multivariate_input,
    validate_univariate_input,
)
#Taken as reference............. Development will continue.






mpl.rc("figure", autolayout=True, dpi=150, figsize=(6.5, 4))
mpl.rc("font", family="serif")
mpl.rc("axes.spines", top=False, right=False)
mpl.rc("axes", titlesize=12, titleweight=500)
mpl.use("agg")
mpl.rc("boxplot", patchartist=True, vertical=False)
mpl.rc("boxplot.medianprops", color="black")


def _savefig(figure: Figure) -> BytesIO:
    graph = BytesIO()
    figure.savefig(graph, format="png")
    return graph


def _get_color_shades_of(color: str, num: int = None) -> Sequence:
    color_rgb = to_rgb(color)
    return np.linspace(color_rgb, (0.25, 0.25, 0.25), num=num)


def box_plot(
    data: Iterable,
    *,
    label: str,
    hue: Iterable = None,
    color: Union[str, Sequence] = None,
):

    original_data = validate_univariate_input(data)
    data = original_data.dropna()

    fig, ax = plt.subplots()

    if hue is None:
        bxplot = ax.boxplot(
            data,
            labels=[label],
            sym=".",
            patch_artist=True,
            boxprops=dict(facecolor=color, alpha=0.75),
        )
        ax.set_yticklabels("")
    else:
        hue = validate_univariate_input(hue)[original_data.notna()]
        groups = {key: series for key, series in data.groupby(hue)}
        bxplot = ax.boxplot(groups.values(), labels=groups.keys(), sym=".")

        if color is None:
            colors = [f"C{idx}" for idx in range(hue.nunique())]
        else:
            colors = _get_color_shades_of(color, hue.nunique())

        for patch, color in zip(bxplot["boxes"], reversed(colors)):
            patch.set_facecolor(color)
            patch.set_alpha(0.75)

    ax.set_title(f"Box-plot of {label}")

    return fig


def kde_plot(
    data: Iterable,
    *,
    label: str,
    hue: Iterable = None,
    color: Union[str, Sequence] = None,
) -> Figure:

    original_data = validate_univariate_input(data)
    data = original_data.dropna()

    fig, ax = plt.subplots()

    if len(data) < 2 or np.isclose(data.std(), 0):
        ax.text(
            x=0.08,
            y=0.45,
            s=(
                "[Could not plot kernel density estimate.\n "
                "Data is singular.]"
            ),
            color="#f72",
            size=14,
            weight=600,
        )
        return fig

    eval_points = np.linspace(data.min(), data.max(), num=len(data))
    if hue is None:
        kernel = gaussian_kde(data)
        density = kernel(eval_points)
        ax.plot(eval_points, density, label=label, color=color)
        ax.fill_between(eval_points, density, alpha=0.3, color=color)
    else:
        hue = validate_univariate_input(hue)[original_data.notna()]
        if color is None:
            colors = [f"C{idx}" for idx in range(hue.nunique())]
        else:
            colors = _get_color_shades_of(color, hue.nunique())

        for color, (key, series) in zip(colors, data.groupby(hue)):
            kernel = gaussian_kde(series)
            density = kernel(eval_points)
            ax.plot(eval_points, density, label=key, alpha=0.75, color=color)
            ax.fill_between(eval_points, density, alpha=0.25, color=color)

    ax.set_ylim(0)
    ax.legend()
    ax.set_title(f"Density plot of {label}")

    return fig


def prob_plot(
    data: Iterable,
    *,
    label: str,
    marker_color: Union[str, Sequence] = "C0",
    line_color: Union[str, Sequence] = "#222",
) -> Figure:

    original_data = validate_univariate_input(data)
    data = original_data.dropna()

    fig, ax = plt.subplots()
    probplot(data, fit=True, plot=ax)
    ax.lines[0].set_color(marker_color)
    ax.lines[1].set_color(line_color)
    ax.set_title(f"Probability plot of {label}")

    return fig


def bar_plot(
    data: Iterable, *, label: str, color: Union[str, Sequence] = None
) -> Figure:

    original_data = validate_univariate_input(data)
    data = original_data.dropna()

    fig, ax = plt.subplots()

    # Include no more than 10 of the most common values
    top_10 = data.value_counts().nlargest(10)
    bars = ax.bar(top_10.index.map(str), top_10, alpha=0.8, color=color)
    ax.bar_label(bars, labels=[f"{x:,.0f}" for x in top_10], padding=2)

    if (num_unique := data.nunique()) > 10:
        title = f"Bar-plot of {label} (Top 10 of {num_unique})"
    else:
        title = f"Bar-plot of {label}"
    ax.set_title(title)
    ax.tick_params(axis="x", rotation=90)  # Improve visibility of long labels

    return fig


def _plot_variable(variables_hue_and_color: Tuple) -> Tuple:

    variable, hue, color = variables_hue_and_color
    if variable.var_type == "numeric":
        graphs = {
            "box_plot": _savefig(
                box_plot(
                    data=variable.data,
                    hue=hue,
                    label=variable.name,
                    color=color,
                )
            ),
            "kde_plot": _savefig(
                kde_plot(
                    data=variable.data,
                    hue=hue,
                    label=variable.name,
                    color=color,
                )
            ),
            "prob_plot": _savefig(
                prob_plot(
                    data=variable.data, label=variable.name, marker_color=color
                )
            ),
        }
    else:  # {"boolean", "categorical", "datetime"}:
        graphs = {
            "bar_plot": _savefig(
                bar_plot(data=variable.data, label=variable.name, color=color)
            )
        }

    return variable.name, graphs


def plot_correlation(
    variables: Iterable,
    max_pairs: int = 20,
    color_pos: Union[str, Sequence] = "orangered",
    color_neg: Union[str, Sequence] = "steelblue",
) -> Figure:

    if not isinstance(variables, MultiVariable):
        variables = MultiVariable(variables)

    if variables._correlation_values is None:
        return None
    pairs_to_show = variables._correlation_values[:max_pairs]
    corr_data = dict(reversed(pairs_to_show))
    labels = [" vs ".join(pair) for pair in corr_data.keys()]

    fig, ax = plt.subplots()
    ax.barh(labels, corr_data.values(), edgecolor="#222", linewidth=0.5)
    ax.set_xlim(-1.1, 1.1)
    ax.spines["left"].set_position("zero")
    ax.yaxis.set_visible(False)  # hide y-axis labels

    for p, label in zip(ax.patches, labels):
        p.set_alpha(min(1, abs(p.get_width()) + 0.1))

        if p.get_width() < 0:
            p.set_facecolor(color_neg)
            ax.text(
                p.get_x(),
                p.get_y() + p.get_height() / 2,
                f"{p.get_width():,.2f} ({label})  ",
                size=8,
                ha="right",
                va="center",
            )
        else:
            p.set_facecolor(color_pos)
            ax.text(
                p.get_x(),
                p.get_y() + p.get_height() / 2,
                f"  {p.get_width():,.2}  ({label})",
                size=8,
                ha="left",
                va="center",
            )

    ax.set_title(f"Pearson Correlation (Top {len(corr_data)})")

    return fig


def regression_plot(
    x: Iterable,
    y: Iterable,
    labels: Tuple[str, str],
    color: Union[str, Sequence] = None,
) -> Figure:

    var1, var2 = labels
    # Convert to DataFrame
    data = validate_multivariate_input({var1: x, var2: y}).dropna()

    if len(data) > 50000:
        data = data.sample(50000)

    fig, ax = plt.subplots()
    x = data[var1]
    y = data[var2]
    slope, intercept = np.polyfit(x, y, deg=1)
    line_x = np.linspace(x.min(), x.max(), num=100)

    ax.scatter(x, y, s=40, alpha=0.7, color=color, edgecolors="#444")
    ax.plot(line_x, slope * line_x + intercept, color="#444", lw=2)
    ax.set_title(
        f"Slope: {slope:,.4f}\nIntercept: {intercept:,.4f}\n"
        + f"Correlation: {x.corr(y):.4f}",
        size=11,
    )
    ax.set_xlabel(var1)
    ax.set_ylabel(var2)

    return fig


def _plot_regression(data_and_color: Tuple) -> Tuple:

    data, color = data_and_color
    var1, var2 = data.columns
    fig = regression_plot(
        x=data[var1], y=data[var2], labels=(var1, var2), color=color
    )
    return (var1, var2), fig


def _plot_multivariable(
    variables: MultiVariable, color: str = None
) -> Optional[Dict]:

    if variables._correlation_values is None:
        return None
    else:
        # Take the top 20 pairs by magnitude of correlation.
        # 20 var_pairs ≈ 10+ pages
        # 20 numeric columns == 190 var_pairs ≈ 95+ pages.
        pairs_to_include = [
            pair for pair, _ in variables._correlation_values[:20]
        ]
        with Pool() as p:
            paired_data_gen = [
                (variables.data.loc[:, pair], color)
                for pair in pairs_to_include
            ]
            bivariate_regression_plots = dict(
                tqdm(
                    # Plot in parallel processes
                    p.imap(_plot_regression, paired_data_gen),
                    # Progress-bar options
                    total=len(pairs_to_include),
                    bar_format=(
                        "{desc} {percentage:3.0f}%|{bar:35}| "
                        "{n_fmt}/{total_fmt} pairs."
                    ),
                    desc="Bivariate analysis:",
                    dynamic_ncols=True,
                )
            )

        return {
            "correlation_plot": _savefig(plot_correlation(variables)),
            "regression_plots": {
                var_pair: _savefig(plot)
                for var_pair, plot in bivariate_regression_plots.items()
            },
        }