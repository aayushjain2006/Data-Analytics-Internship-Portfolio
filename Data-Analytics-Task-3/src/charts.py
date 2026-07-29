import os
import matplotlib.pyplot as plt

# Create output folders if they don't exist
os.makedirs("Output/charts", exist_ok=True)


def save_bar_chart(data, title, xlabel, ylabel, filename):
    plt.figure(figsize=(10, 6))
    data.plot(kind="bar")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"Output/charts/{filename}")
    plt.close()


def save_line_chart(data, title, xlabel, ylabel, filename):
    plt.figure(figsize=(12, 6))
    data.plot(kind="line", marker="o")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"Output/charts/{filename}")
    plt.close()


def save_pie_chart(data, title, filename):
    plt.figure(figsize=(8, 8))
    data.plot(kind="pie", autopct="%1.1f%%")
    plt.ylabel("")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(f"Output/charts/{filename}")
    plt.close()