import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from sports_etl.config import WATERMARK_PATH, DEFAULT_WATERMARK_POSITION


def get_team_palette():
    return {
        "ATL": "#C8102E", "CHI": "#418FDE", "CON": "#DC4405", "DAL": "#0c2340",
        "GSV": "#AD96DC", "IND": "#C8102E", "LAS": "#702F8A", "LVA": "#000000", "MIN": "#0C2340",
        "NYL": "#6ECEB2", "PHO": "#201747", "SEA": "#2C5234", "WAS": "#c8102e"
    }


def get_team_secondary_color(team):
    secondary_colors = {
        "ATL": "#418FDE", "CHI": "#FFCD00", "CON": "#041e42", "DAL": "#c4d600",
        "GSV": "#000000", "IND": "#041E42", "LAS": "#FFC72C", "LVA": "#8A8D8F", "MIN": "#78BE20",
        "NYL": "#000000", "PHO": "#CB6015", "SEA": "#FBE122", "WAS": "#0c2340"
    }
    return secondary_colors.get(team, "#CCCCCC")  # fallback color


def get_wnba_brand_colors():
    return {
        "primary": "#F57B20",    # princeton orange
        "secondary": "#050707",  # vampire black
        "neutral": "#EFE3C6",    # pearl
        "gray": "#4C4C4D"        # quartz
    }

def apply_playher_watermark(ax, position="bottom-right"):
    """
    Adds a simple 'via playher.ai' text watermark to a matplotlib Axes.

    Parameters:
        ax (matplotlib.axes.Axes): The axes to add the watermark to.
        position (str): One of "bottom-right", "bottom-left", "top-left", "top-right".
    """
    pos_map = {
        "bottom-right": (0.99, -0.2, 'right'),
        "bottom-left": (0.01, -0.2, 'left'),
        "top-left": (0.01, 1.05, 'left'),
        "top-right": (0.99, 1.05, 'right'),
    }

    if position not in pos_map:
        raise ValueError(f"Invalid position: {position}")

    x, y, ha = pos_map[position]
    ax.text(
        x, y, "via playher.ai",
        transform=ax.transAxes,
        ha=ha, va='top',
        fontsize=8, alpha=0.6
    )