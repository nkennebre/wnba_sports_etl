import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from sports_etl.config import DEFAULT_WATERMARK_POSITION


def get_nwsl_brand_colors():
    return {
        "primary": "#0C2340",    # blue
        "secondary": "#C8102E",  # red
        "neutral": "#B1B3B3",    # grey
        "lilac": "#FFFFFF",        # white
    }

def get_pwhl_brand_colors():
    return {
        "primary": "#9e7dc5",    # lavender purple
        "secondary": "#230f62",  # dark purple
        "neutral": "#ffffff",    # white
        "lilac": "#c8a2c8",        # lilac
        "blue": "#b0e0e6",        # icy blue
    }
 
def get_wnba_brand_colors():
    return {
        "primary": "#F57B20",    # princeton orange
        "secondary": "#050707",  # vampire black
        "neutral": "#EFE3C6",    # pearl
        "gray": "#4C4C4D"        # quartz 
    }
  

def get_team_palette_nwsl(): # new teams (BOS, verify colors, new club)
    return {
        "LA": "#010101", "BAY": "#051C2C", "BOS": "#852734", "CHI": "#051C2C",
        "HOU": "#FF6900", "KC": "#CB333B", "GFC": "#9ADBE8", "NC": "#01426A",
        "ORL": "#5F249F", "POR": "#93282C", "LOU": "#C5B4E3", "SD": "#00C1D4",
        "SEA": "#003087", "UTA": "#001E62", "WAS": "#C8102E"
    }

def get_team_palette_pwhl(): # new teams (VAN and SEA, verify colors)
    return {
        "BOS": "#153f36", "MIN": "#9e7dc5", "MON": "#852734", "NY": "#00b9b3",
        "OTT": "#a51b2f", "SEA": "#000000", "TOR": "#307fe2", "VAN": "#0A5B69"
    }
    
def get_team_palette_wnba():
    return {
        "ATL": "#C8102E", "CHI": "#418FDE", "CON": "#DC4405", "DAL": "#0c2340",
        "GSV": "#AD96DC", "IND": "#C8102E", "LAS": "#702F8A", "LVA": "#000000", "MIN": "#0C2340",
        "NYL": "#6ECEB2", "PHO": "#201747", "SEA": "#2C5234", "WAS": "#c8102e"
    }
 
def get_team_secondary_color_nwsl(team):
    secondary_colors = {
        "LA": "#F2D4D7", "BAY": "#F9423A", "BOS": "#852734", "CHI": "#41B6E6",
        "HOU": "#8BB8E8", "KC": "#091F2C", "GFC": "#010101", "NC": "#A50034",
        "ORL": "#00A9E0", "POR": "#215732", "LOU": "#1E1A34", "SD": "#E31C79",
        "SEA": "#D22730", "UTA": "#9D2235", "WAS": "#051C2C"
    }
    return secondary_colors.get(team, "#CCCCCC")  # fallback color
 
def get_team_secondary_color_pwhl(team):
    secondary_colors = {
        "BOS": "#b3e2d8", "MIN": "#230f62", "MON": "#011e42", "NY": "#011e42",
        "OTT": "#fdb81e", "SEA": "#084639", "TOR": "#ffb81c", "VAN": "#000000"
    }
    return secondary_colors.get(team, "#CCCCCC")  # fallback color
  
def get_team_secondary_color_wnba(team):
    secondary_colors = {
        "ATL": "#418FDE", "CHI": "#FFCD00", "CON": "#041e42", "DAL": "#c4d600",
        "GSV": "#000000", "IND": "#041E42", "LAS": "#FFC72C", "LVA": "#8A8D8F", "MIN": "#78BE20",
        "NYL": "#000000", "PHO": "#CB6015", "SEA": "#FBE122", "WAS": "#0c2340"
    }
    return secondary_colors.get(team, "#CCCCCC")  # fallback color
   
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
    
def get_team_palette(league: str = "wnba") -> dict:
    league = league.lower()
    if league == "wnba":
        return get_team_palette_wnba()
    elif league == "nwsl":
        return get_team_palette_nwsl()
    elif league == "pwhl":
        return get_team_palette_pwhl()
    else:
        raise ValueError(f"Unsupported league: {league}")

def get_team_secondary_color(league: str, team: str) -> str:
    league = league.lower()
    if league == "wnba":
        return get_team_secondary_color_wnba(team)
    elif league == "nwsl":
        return get_team_secondary_color_nwsl(team)
    elif league == "pwhl":
        return get_team_secondary_color_pwhl(team)
    else:
        raise ValueError(f"Unsupported league: {league}")
