from reportlab.lib.units import cm
from reportlab.lib import colors
from Bio.Graphics import GenomeDiagram
from Bio import SeqIO

# Parses the given file
record = SeqIO.read("Genome.gb", "genbank")

# Adds track to the provided PNG
gd_diagram = GenomeDiagram.Diagram("DNA Sequence for Virus")
gd_track_for_features = gd_diagram.new_track(1, name="Annotated Features")
gd_feature_set = gd_track_for_features.new_set()

# Traverses through the given DNA sequence and colorizes them
for feature in record.features:
    if feature.type != "gene":
        continue
    if len(gd_feature_set) % 2 == 0:
        color = colors.red
    else:
        color = colors.lightsalmon

    # Adds features to track
    gd_feature_set.add_feature(feature, color=color, label_position="middle", label=True, label_size=17,
                               label_color=color)

# Provides formatting for the DNA visualization within the PNG
gd_diagram.draw(format="circular", circular=True, pagesize=(25 * cm, 25 * cm), start=0, end=len(record),
                circle_core=0.65)

# Creates the PNG file
gd_diagram.write("dnaSequence.png", "PNG")
