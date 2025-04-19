from mango_app.PestDisease import PestDisease

pd_1 = PestDisease(
    "Fruit Fly",
    "Pest",
    "Harmful pest that damages mangoes by depositing eggs in developing fruits.",
    "The *Bactrocera dorsalis* fruit fly species poses a major threat to mango production. Female flies pierce the fruit skin to lay eggs, and the hatched maggots tunnel through the flesh, leading to fruit rot and early dropping. Effective management requires integrated pest control including monitoring traps, protein baits, and proper orchard sanitation.",
    "fruit_fly.jpg"
)

pd_2 = PestDisease(
    "Bacterial Black Spot",
    "Disease",
    "A bacterial infection causing black lesions on mango leaves, fruit, and stems.",
    "Bacterial Black Spot is caused by *Xanthomonas campestris*. It appears as black, water-soaked lesions. The disease is spread by wind, rain, and contaminated tools. Copper-based fungicides and proper sanitation can help manage this disease.",
    "bacterial_black_spot.jpg"
)

pd_3 = PestDisease(
    "Anthracnose",
    "Disease", 
    "Fungal infection creating dark spots and lesions across mango plant tissues.",
    "The fungal pathogen *Colletotrichum gloeosporioides* causes Anthracnose disease in mangoes. It manifests as black necrotic areas on foliage, blossoms and fruit surfaces. Disease development accelerates in wet, humid environments, particularly during flowering and fruit development. Control measures include canopy management and targeted fungicide programs.",
    "anthracnose.jpg"
)


pd_4 = PestDisease(
    "Mango Leafhopper",
    "Pest",
    "A small insect that sucks sap from mango tree leaves.",
    "Mango leafhoppers (*Idioscopus clypealis*) cause yellowing of mango leaves and contribute to premature leaf drop. They also spread diseases like powdery mildew. Insecticides and removing affected leaves help control this pest.",
    "mango_leafhopper.jpg"
)

pd_5 = PestDisease(
    "Mango Weevil",
    "Pest",
    "A major pest that infests mangoes, causing the fruit to rot.",
    "The mango weevil (*Sternochetus mangiferae*) bores into mango fruit to lay eggs, which causes the fruit to rot. The larvae feed on the fruit, leading to decay. Traps and insecticides are effective in controlling mango weevil.",
    "mango_weevil.jpg"
)

pd_6 = PestDisease(
    "Mealybugs",
    "Pest",
    "Cotton-like insects that colonize and feed on plant parts in groups.",
    "These sap-feeding pests form white, waxy colonies on stems and leaves. Their feeding reduces plant vigor while promoting ant activity and sooty mold growth. Successful control combines physical removal, beneficial insect conservation, and targeted chemical interventions when necessary.",
    "mealybugs.jpg"
)

pd_7 = PestDisease(
    "Sooty Mold",
    "Disease",
    "Secondary fungal infection creating dark film on plant surfaces.",
    "This opportunistic fungus develops on honeydew excretions from sap-feeding insects. While not directly harmful to the plant, the black coating interferes with photosynthesis and reduces plant productivity. Management focuses on controlling the underlying insect infestations.",
    "sooty_mold.jpg"
)

pest_diseases_list = [pd_1, pd_2, pd_3, pd_4, pd_5, pd_6, pd_7]
