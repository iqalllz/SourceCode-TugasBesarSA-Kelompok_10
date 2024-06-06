import matplotlib.pyplot as plt

# Daftar kegiatan
activities = [
    {"name": "Kegiatan 1", "category": "A"},
    {"name": "Kegiatan 2", "category": "A"},
    {"name": "Kegiatan 3", "category": "B"},
    {"name": "Kegiatan 4", "category": "B"},
    {"name": "Kegiatan 5", "category": "C"},
]

# Mengelompokkan kegiatan berdasarkan kategori
activities_by_category = {}
for activity in activities:
    category = activity["category"]
    if category not in activities_by_category:
        activities_by_category[category] = []
    activities_by_category[category].append(activity["name"])

# Membuat gambar menggunakan Matplotlib
plt.figure(figsize=(8, 6))
for i, (category, activities) in enumerate(activities_by_category.items()):
    plt.text(0.1, 0.9 - i * 0.1, f"{category}: {', '.join(activities)}", fontsize=12)

# Mengatur tata letak dan label
plt.axis("off")

# Menyimpan gambar sebagai file
plt.savefig("activities.png", bbox_inches="tight")
