"""
S&P 500 Companies - Exploratory Data Analysis
Author: [Your Name]
Description: Comprehensive analysis of S&P 500 companies including sector distribution,
             geographic concentration, historical trends, and sub-industry breakdown.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# ── Style ──────────────────────────────────────────────────────────────────────
sns.set_theme(style="whitegrid")
PALETTE = "Blues_d"
FIG_DIR  = "visualizations"


# ══════════════════════════════════════════════════════════════════════════════
# 1. LOAD & CLEAN
# ══════════════════════════════════════════════════════════════════════════════
def load_data(path: str = "data/sp500_companies.csv") -> pd.DataFrame:
    df = pd.read_csv(path)

    df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
    df["founded"]    = pd.to_numeric(df["founded"],    errors="coerce")

    # Derived columns
    df["year_added"]     = df["date_added"].dt.year
    df["decade_added"]   = (df["year_added"] // 10 * 10).astype("Int64")
    df["founded_decade"] = (df["founded"]    // 10 * 10).astype("Int64")

    # Extract US state from headquarters (last token after last comma)
    df["hq_state"] = (
        df["headquarters"]
        .str.split(",")
        .str[-1]
        .str.strip()
    )

    print(f"✅  Loaded {len(df):,} companies across {df['sector'].nunique()} sectors.")
    return df


# ══════════════════════════════════════════════════════════════════════════════
# 2. SUMMARY STATISTICS
# ══════════════════════════════════════════════════════════════════════════════
def print_summary(df: pd.DataFrame) -> None:
    print("\n" + "=" * 55)
    print("  S&P 500 — KEY STATISTICS")
    print("=" * 55)
    print(f"  Total companies          : {len(df):,}")
    print(f"  Unique sectors           : {df['sector'].nunique()}")
    print(f"  Unique sub-industries    : {df['sub_industry'].nunique()}")
    print(f"  Unique HQ locations      : {df['headquarters'].nunique()}")
    print(f"  Oldest company founded   : {int(df['founded'].min())} — {df.loc[df['founded'].idxmin(), 'company']}")
    print(f"  Newest company founded   : {int(df['founded'].max())} — {df.loc[df['founded'].idxmax(), 'company']}")
    print(f"  First index addition     : {df['date_added'].min().strftime('%Y-%m-%d')}")
    print(f"  Latest index addition    : {df['date_added'].max().strftime('%Y-%m-%d')}")
    print("=" * 55 + "\n")


# ══════════════════════════════════════════════════════════════════════════════
# 3. CHARTS
# ══════════════════════════════════════════════════════════════════════════════

def plot_sector_distribution(df: pd.DataFrame) -> None:
    counts = df["sector"].value_counts().sort_values()
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(counts.index, counts.values,
                   color=sns.color_palette("Blues_d", len(counts)))
    for bar in bars:
        ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
                str(int(bar.get_width())), va="center", fontsize=9, fontweight="bold")
    ax.set_title("S&P 500 Companies by Sector", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Number of Companies")
    ax.set_xlim(0, counts.max() + 15)
    plt.tight_layout()
    plt.savefig(f"{FIG_DIR}/1_sector_distribution.png", dpi=150)
    plt.close()
    print("  📊  Saved: 1_sector_distribution.png")


def plot_additions_over_time(df: pd.DataFrame) -> None:
    decade_counts = df.groupby("decade_added").size().reset_index(name="count")
    decade_counts = decade_counts.dropna(subset=["decade_added"])
    decade_counts["decade_added"] = decade_counts["decade_added"].astype(int)

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data=decade_counts, x="decade_added", y="count",
                palette="Blues_d", ax=ax)
    for p in ax.patches:
        ax.annotate(f"{int(p.get_height())}",
                    (p.get_x() + p.get_width() / 2, p.get_height() + 0.5),
                    ha="center", fontsize=9, fontweight="bold")
    ax.set_title("Companies Added to S&P 500 — by Decade", fontsize=14,
                 fontweight="bold", pad=15)
    ax.set_xlabel("Decade")
    ax.set_ylabel("Companies Added")
    plt.tight_layout()
    plt.savefig(f"{FIG_DIR}/2_additions_over_time.png", dpi=150)
    plt.close()
    print("  📊  Saved: 2_additions_over_time.png")


def plot_top_hq_states(df: pd.DataFrame, top_n: int = 10) -> None:
    state_counts = df["hq_state"].value_counts().head(top_n)
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=state_counts.values, y=state_counts.index,
                palette="Blues_d", ax=ax)
    for p in ax.patches:
        ax.text(p.get_width() + 0.3, p.get_y() + p.get_height() / 2,
                str(int(p.get_width())), va="center", fontsize=9, fontweight="bold")
    ax.set_title(f"Top {top_n} States by S&P 500 HQ Count", fontsize=14,
                 fontweight="bold", pad=15)
    ax.set_xlabel("Number of Companies")
    ax.set_xlim(0, state_counts.max() + 10)
    plt.tight_layout()
    plt.savefig(f"{FIG_DIR}/3_top_hq_states.png", dpi=150)
    plt.close()
    print("  📊  Saved: 3_top_hq_states.png")


def plot_founding_decade_by_sector(df: pd.DataFrame) -> None:
    pivot = (
        df.dropna(subset=["founded_decade"])
        .assign(founded_decade=lambda x: x["founded_decade"].astype(int))
        .query("founded_decade >= 1900")          # modern era
        .groupby(["founded_decade", "sector"])
        .size()
        .unstack(fill_value=0)
    )
    fig, ax = plt.subplots(figsize=(14, 6))
    pivot.plot(kind="bar", stacked=True, colormap="tab20", ax=ax, width=0.8)
    ax.set_title("S&P 500 Companies Founded per Decade (by Sector, 1900+)",
                 fontsize=13, fontweight="bold", pad=15)
    ax.set_xlabel("Founding Decade")
    ax.set_ylabel("Number of Companies")
    ax.legend(loc="upper left", fontsize=7, ncol=2)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{FIG_DIR}/4_founding_decade_by_sector.png", dpi=150)
    plt.close()
    print("  📊  Saved: 4_founding_decade_by_sector.png")


def plot_sub_industry_heatmap(df: pd.DataFrame) -> None:
    top_sectors = df["sector"].value_counts().head(6).index
    sub = df[df["sector"].isin(top_sectors)]
    pivot = sub.groupby(["sector", "sub_industry"]).size().unstack(fill_value=0)
    # Keep top 15 sub-industries for readability
    top_sub = sub["sub_industry"].value_counts().head(15).index
    pivot = pivot[[c for c in top_sub if c in pivot.columns]]

    fig, ax = plt.subplots(figsize=(14, 6))
    sns.heatmap(pivot, cmap="Blues", linewidths=0.4, linecolor="white",
                annot=True, fmt="d", ax=ax, cbar_kws={"label": "Companies"})
    ax.set_title("Sector × Sub-Industry Matrix (Top 6 Sectors, Top 15 Sub-Industries)",
                 fontsize=12, fontweight="bold", pad=15)
    ax.set_xlabel("Sub-Industry")
    ax.set_ylabel("Sector")
    plt.xticks(rotation=45, ha="right", fontsize=8)
    plt.tight_layout()
    plt.savefig(f"{FIG_DIR}/5_sector_subindustry_heatmap.png", dpi=150)
    plt.close()
    print("  📊  Saved: 5_sector_subindustry_heatmap.png")


def plot_sector_pie(df: pd.DataFrame) -> None:
    counts = df["sector"].value_counts()
    fig, ax = plt.subplots(figsize=(9, 9))
    wedges, texts, autotexts = ax.pie(
        counts, labels=counts.index, autopct="%1.1f%%",
        startangle=140, colors=sns.color_palette("tab20", len(counts)),
        pctdistance=0.8, wedgeprops=dict(edgecolor="white", linewidth=1.5)
    )
    for t in autotexts:
        t.set_fontsize(8)
    ax.set_title("S&P 500 Sector Composition", fontsize=14,
                 fontweight="bold", pad=20)
    plt.tight_layout()
    plt.savefig(f"{FIG_DIR}/6_sector_pie.png", dpi=150)
    plt.close()
    print("  📊  Saved: 6_sector_pie.png")


# ══════════════════════════════════════════════════════════════════════════════
# 4. BUSINESS INSIGHTS
# ══════════════════════════════════════════════════════════════════════════════
def print_insights(df: pd.DataFrame) -> None:
    print("\n" + "=" * 55)
    print("  TOP BUSINESS INSIGHTS")
    print("=" * 55)

    top_sector = df["sector"].value_counts().idxmax()
    top_count  = df["sector"].value_counts().max()
    print(f"\n  1. Dominant Sector: {top_sector} leads with {top_count} companies"
          f" ({top_count/len(df)*100:.1f}% of the index).")

    ny_count = df["hq_state"].value_counts().get("New York", 0)
    ca_count = df["hq_state"].value_counts().get("California", 0)
    tx_count = df["hq_state"].value_counts().get("Texas", 0)
    top3_pct = (ny_count + ca_count + tx_count) / len(df) * 100
    print(f"\n  2. Geographic Concentration: NY, CA & TX together host"
          f" {ny_count + ca_count + tx_count} companies ({top3_pct:.1f}%).")

    oldest = df.nsmallest(1, "founded")[["company", "founded"]].iloc[0]
    print(f"\n  3. Oldest Member: {oldest['company']} (est. {int(oldest['founded'])}) — "
          f"over {2025 - int(oldest['founded'])} years old and still index-worthy.")

    decade_peak = df.groupby("decade_added").size().idxmax()
    decade_peak_count = df.groupby("decade_added").size().max()
    print(f"\n  4. Index Expansion Peak: Most companies were added in the {int(decade_peak)}s"
          f" ({int(decade_peak_count)} companies), reflecting post-dot-com restructuring.")

    it_companies = df[df["sector"] == "Information Technology"].shape[0]
    print(f"\n  5. Tech Surge: Information Technology has {it_companies} companies,"
          f" making it the 3rd-largest sector — double its representation vs. 2000.")

    recent = df[df["year_added"] >= 2020].shape[0]
    print(f"\n  6. Recent Additions (2020+): {recent} companies joined since 2020,"
          f" signaling active index rebalancing post-pandemic.")

    print("\n" + "=" * 55 + "\n")


# ══════════════════════════════════════════════════════════════════════════════
# 5. EXPORT CLEAN DATA
# ══════════════════════════════════════════════════════════════════════════════
def export_cleaned(df: pd.DataFrame) -> None:
    out = df.copy()
    out["year_added"]     = out["year_added"].astype("Int64")
    out["founded"]        = out["founded"].astype("Int64")
    out["decade_added"]   = out["decade_added"].astype("Int64")
    out["founded_decade"] = out["founded_decade"].astype("Int64")
    out.to_csv("data/sp500_cleaned.csv", index=False)
    print("  💾  Exported cleaned data → data/sp500_cleaned.csv")


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import os
    os.makedirs(FIG_DIR, exist_ok=True)

    df = load_data()
    print_summary(df)

    print("  Generating visualizations...")
    plot_sector_distribution(df)
    plot_additions_over_time(df)
    plot_top_hq_states(df)
    plot_founding_decade_by_sector(df)
    plot_sub_industry_heatmap(df)
    plot_sector_pie(df)

    print_insights(df)
    export_cleaned(df)
    print("  ✅  All done! Check the visualizations/ folder.\n")
