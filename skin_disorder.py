import streamlit as st
import pickle
import numpy as np

def round_to_thousands(number):
    return round(number, -3)


def main():
    # Load the model
    model1 = pickle.load(open("skin_disorder_predction.pkl", "rb"))

    # Numeric mapping for categorical variables
    erythema_level = {
        "Select erythema level":"",
         "not present": 0,
        "Mild level": 1,
        "Moderate level": 2,
        "Severe level": 3,
    }

    scaling_level = {
        "Select scaling level ":"",
         "not present": 0,
        "Mild level": 1,
        "Moderate level": 2,
        "Severe level": 3,
    }

    definite_borders_level = {
        "Select definite borders level ":"",
         "not present": 0,
        "Mild level": 1,
        "Moderate level": 2,
        "Severe level": 3,
    }

    itching_level = {
        "Select itching level ":"",
         "not present": 0,
        "Mild level": 1,
        "Moderate level": 2,
        "Severe level": 3,
    }

    koebner_phenomenon_level = {
        "Select koebner phenomenon level ":"",
         "not present": 0,
        "Mild level": 1,
        "Moderate level": 2,
        "Severe level": 3,
    }

    Follicular_papules_level = {
        "Follicular papules level ":"",
         "not present": 0,
        "Mild level": 1,
        "Moderate level": 2,
        "Severe level": 3,
    }

    elbow_involvement_level = {
        "Select elbow involvement level ":"",
         "not present": 0,
        "Mild level": 1,
        "Moderate level": 2,
        "Severe level": 3,
    }

    scalp_involvement_level = {
        "Select scalp involvement level ":"",
         "not present": 0,
        "Mild level": 1,
        "Moderate level": 2,
        "Severe level": 3,
    }

    family_history = {
        "Select family history ":"",
        'No': 0,
        'Yes': 1

    }

    eosinophils_in_the_infiltrate_level = {
        "eosinophils in the infiltrate level ":"",
         "not present": 0,
        "Mild level": 1,
        "Moderate level": 2,
        "Severe level": 3,
    }

    PNL_infiltrate_level = {
        "PNL infiltrate level ":"",
         "not present": 0,
        "Mild level": 1,
        "Moderate level": 2,
        "Severe level": 3,
    }

    fibrosis_of_the_papillary_dermis_level = {
        "Select fibrosis of the papillary dermis level":"",
         "not present": 0,
        "Mild level": 1,
        "Moderate level": 2,
        "Severe level": 3,
    }

    exocytosis_level = {
        "Select exocytosis level ":"",
         "not present": 0,
        "Mild level": 1,
        "Moderate level": 2,
        "Severe level": 3,
    }

    acanthosis_level = {
        "Select acanthosis level ":"",
         "not present": 0,
        "Mild level": 1,
        "Moderate level": 2,
        "Severe level": 3,
    }

    hyperkeratosis_level = {
        "Select hyperkeratosis level: ":"",
         "not present": 0,
        "Mild level": 1,
        "Moderate level": 2,
        "Severe level": 3,
    }

    parakeratosis_level = {
        "Select parakeratosis level ":"",
         "not present": 0,
        "Mild level": 1,
        "Moderate level": 2,
        "Severe level": 3,
    }

    elongation_of_the_rete_ridges_level = {
        "Select elongation of the rete ridges levell ":"",
         "not present": 0,
        "Mild level": 1,
        "Moderate level": 2,
        "Severe level": 3,
    }

    spongiform_pustule_level = {
        "Select spongiform pustule level ":"",
         "not present": 0,
        "Mild level": 1,
        "Moderate level": 2,
        "Severe level": 3,
    }

    munro_microabcess_level = {
        "Select munro microabcess level ":"",
         "not present": 0,
        "Mild level": 1,
        "Moderate level": 2,
        "Severe level": 3,
    }

    disappearance_of_the_granular_layer_level = {
        "Select disappearance of the granular layer level ":"",
         "not present": 0,
        "Mild level": 1,
        "Moderate level": 2,
        "Severe level": 3,
    }

    spongiosis_level = {
        "Select spongiosis level ":"",
         "not present": 0,
        "Mild level": 1,
        "Moderate level": 2,
        "Severe level": 3,
    }

    inflammatory_mononuclear_infiltrate_level = {
        "Select inflammatory mononuclear infiltrate level ":"",
         "not present": 0,
        "Mild level": 1,
        "Moderate level": 2,
        "Severe level": 3,
    }

    

    # Title with background
    st.title("Welcome to  Skin disorder Prediction")
    
    st.subheader("Problem Statement:")
    st.write("Create a predictive model using machine learning techniques to predict the various classes ofskin disease. Suggestions to the Doctors to identify the skin diseases of the patientat the earliest.")
    st.write("Please choose the information from the collection below to check the patient skin disease.")

    col1, col2, col3  = st.columns(3)

    with col1:
        erythema_level1 = st.selectbox("Select erythema level:", list(erythema_level.keys()))
        scaling_level1 = st.selectbox("Select scaling level:", list(scaling_level.keys()))
        definite_borders_level1 = st.selectbox("Select definite borders level:", list(definite_borders_level.keys()))
        itching_level1 = st.selectbox("Select itching level:", list(itching_level.keys()))
        koebner_phenomenon_level1 = st.selectbox("Select koebner phenomenon level:", list(koebner_phenomenon_level.keys()))
        parakeratosis_level1 = st.selectbox("Select parakeratosis level:", list(parakeratosis_level.keys()))
        elongation_of_the_rete_ridges_level1 = st.selectbox("Select elongation of the rete ridges level:", list(elongation_of_the_rete_ridges_level.keys()))
        spongiform_pustule_level1 = st.selectbox("Select spongiform pustule level:", list(spongiform_pustule_level.keys()))
        
    with col2:
        Follicular_papules_level1 = st.selectbox("Select Follicular papules level:", list(Follicular_papules_level.keys()))
        elbow_involvement_level1 = st.selectbox("Select elbow involvement level:", list(elbow_involvement_level.keys()))
        scalp_involvement_level1 = st.selectbox("Select scalp involvement level:", list(scalp_involvement_level.keys()))
        family_history1 = st.selectbox("Select family history:", list(family_history.keys()))
        eosinophils_in_the_infiltrate_level1 = st.selectbox("Select eosinophils in the infiltrate level:", list(eosinophils_in_the_infiltrate_level.keys()))
        munro_microabcess_level1 = st.selectbox("Select munro microabcess level:", list(munro_microabcess_level.keys()))
        disappearance_of_the_granular_layer_level1 = st.selectbox("Select disappearance of the granular layer level:", list(disappearance_of_the_granular_layer_level.keys()))
        user_age = st.number_input("Enter Patient Age", value=35, min_value=1, max_value=120)
    
    with col3:
        PNL_infiltrate_level1 = st.selectbox("Select PNL infiltrate level:", list(PNL_infiltrate_level.keys()))
        fibrosis_of_the_papillary_dermis_level1 = st.selectbox("Select fibrosis of the papillary dermis level:", list(fibrosis_of_the_papillary_dermis_level.keys()))
        exocytosis_level1 = st.selectbox("Select exocytosis level:", list(exocytosis_level.keys()))
        acanthosis_level1 = st.selectbox("Select acanthosis level:", list(acanthosis_level.keys()))
        hyperkeratosis_level1 = st.selectbox("Select hyperkeratosis level:", list(hyperkeratosis_level.keys()))
        spongiosis_level1 = st.selectbox("Select spongiosis level:", list(spongiosis_level.keys()))
        inflammatory_mononuclear_infiltrate_level1 = st.selectbox("Select inflammatory mononuclear infiltrate level:", list(inflammatory_mononuclear_infiltrate_level.keys()))


    submit_button = st.button("Predict Skin Disorder")
    prediction = None
    if submit_button:
        input_data =[erythema_level[erythema_level1], scaling_level[scaling_level1], definite_borders_level[definite_borders_level1],itching_level[itching_level1],koebner_phenomenon_level[koebner_phenomenon_level1],
                    Follicular_papules_level[Follicular_papules_level1], elbow_involvement_level[elbow_involvement_level1], scalp_involvement_level[scalp_involvement_level1],family_history[family_history1],eosinophils_in_the_infiltrate_level[eosinophils_in_the_infiltrate_level1],
                    PNL_infiltrate_level[PNL_infiltrate_level1], fibrosis_of_the_papillary_dermis_level[fibrosis_of_the_papillary_dermis_level1], exocytosis_level[exocytosis_level1],acanthosis_level[acanthosis_level1],hyperkeratosis_level[hyperkeratosis_level1], 
                    parakeratosis_level[parakeratosis_level1], elongation_of_the_rete_ridges_level[elongation_of_the_rete_ridges_level1], spongiform_pustule_level[spongiform_pustule_level1],munro_microabcess_level[munro_microabcess_level1],disappearance_of_the_granular_layer_level[disappearance_of_the_granular_layer_level1], 
                    spongiosis_level[spongiosis_level1], inflammatory_mononuclear_infiltrate_level[inflammatory_mononuclear_infiltrate_level1],user_age]

        final_input = np.array(input_data)
        prediction = model1.predict([final_input])[0]

    # Mapping dictionary for prediction values to skin disorder names
        prediction_mapping = {
            1: "psoriasis",
            2: "seborrheic dermatitis",
            3: "lichen planus",
            4: "pityriasis rosea",
            5: "chronic dermatitis",
            6: "pityriasis rubra pilaris"
            }

    # Get the predicted skin disorder name
        predicted_skin_disorder = prediction_mapping.get(prediction, "Unknown")
        st.subheader(f"The patient is suffering from {predicted_skin_disorder} type of skin disease") 



    st.subheader("TYPES OF DISEASE IN THIS PROJECT")
    st.write("The diseases in this group are psoriasis, seboreic dermatitis, lichen planus, pityriasis rosea, cronic dermatitis, and pityriasis rubra pilaris.")
    st.subheader("Disease Represented:")
    
    st.write("")

    col01, col02, col03  = st.columns(3)

    with col01:
        st.write("1. Psoriasis Disease")
        image_url1 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSTc5Vor1XgCHmU77FzqrZTID87kA7zFWtFlA&usqp=CAU"
        st.image(image_url1)
        st.write("4. pityriasis rosea Disease")
        image_url4 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmK82YtGsXzkWozJ16udQ-iu_PcNYeO5cTXA&usqp=CAU"
        st.image(image_url4)
        
    with col02:
        st.write("2. Seboreic dermatitis Disease")
        image_url2 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbavESiZvnvBGVhvuSdhN5FipnJo2bNNm8tQ&usqp=CAU"
        st.image(image_url2)
        st.write("5. cronic dermatitis Disease")
        image_url5 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTAPCoKMgLsfQSkdvscI9DdOXLVPwH6T0SxZw&usqp=CAU"
        st.image(image_url5)
        
        
    
    with col03:
        st.write("3. Lichen planus Disease")
        image_url3 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZOWJAnYiXrAWIJ_dIsh6a9fa1IMxxbCZ8ZQ&usqp=CAU"
        st.image(image_url3) 
        st.write("6. pityriasis rubra pilaris Disease")
        image_url6 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmmT41XaAErTUrOjwJ-VJOFHq0u-7D-WN6Pw&usqp=CAU"
        st.image(image_url6)

    st.subheader("ABOUT EACH FEATURES:")
# Header
    st.header("Difference Between Clinical And Histopathological")

    # Paragraph 1
    st.write("Clinical and histopathological evaluations are two complementary approaches used in the diagnosis and assessment of skin disorders."
            " Here are the key differences between the two:")

    # Header 1
    st.subheader("Clinical Evaluation:")
    # Paragraphs under Header 1
    st.write("1. Clinical evaluation involves examining the patient's skin visually and assessing the symptoms and physical characteristics of the skin disorder."
            " It is based on the observation of external signs, such as rash, redness, swelling, texture changes, blistering, scaling, and other visible abnormalities.")
    st.write("2. It is based on the observation of external signs, such as rash, redness, swelling, texture changes, blistering, scaling, and other visible abnormalities.")
    st.write("3. Clinical evaluation is typically performed by dermatologists or healthcare professionals through a physical examination and patient history.")
    st.write("4. It focuses on identifying patterns, distribution, and overall appearance of skin lesions to make a preliminary diagnosis and determine the course of treatment.")
    st.write("5. Clinical evaluation is non-invasive and can be performed during a routine clinical visit.")

    # Header 2
    st.subheader("Histopathological Evaluation:")
    # Paragraphs under Header 2
    st.write("1. Histopathological evaluation involves the microscopic examination of skin tissue samples (biopsies) obtained from the affected area."
            " It is performed by a pathologist who analyzes the cellular and tissue changes at a microscopic level.")
    st.write("2. The biopsy sample is processed, embedded in paraffin, and stained before being examined under a microscope.")
    st.write("3. Histopathological evaluation provides detailed information about the cellular composition, structural changes, and inflammatory processes occurring within the skin.")
    st.write("4. It helps in confirming or refining the diagnosis, assessing the disease severity, and identifying specific histological features associated with different skin disorders.")
    st.write("5. Histopathological evaluation is invasive, requiring the collection of tissue samples, and is usually performed when clinical findings are inconclusive or to monitor disease progression.")

    # Header 3
    st.subheader("1. Erythema")
    # Paragraph under Header 3
    st.write("Erythema is a term used to describe redness or reddening of the skin. It is a common clinical finding that can be associated with various skin conditions and underlying causes."
            " Erythema occurs due to increased blood flow to the skin, often resulting from inflammation, dilation of blood vessels, or increased blood flow in the affected area."
            " Here are a few examples of skin conditions where erythema may be observed: Sunburn, Dermatitis, Infections, Autoimmune diseases, Allergic reactions.")

    # Header 4
    st.subheader("2. Scaling")
    # Paragraph under Header 4
    st.write("Scaling refers to the presence of visible flakes or dry skin that can occur on the surface of the skin."
            " It is a common symptom associated with several skin conditions and can vary in severity and appearance."
            " Scaling occurs when there is an abnormal or accelerated process of skin cell turnover and shedding."
            " Here are a few examples of skin conditions where scaling may be observed: Dry skin (Xerosis), Psoriasis, Seborrheic dermatitis, Fungal infections, Ichthyosis."
            " Scaling can also occur as a secondary symptom in other skin conditions, such as eczema, contact dermatitis, or certain types of skin infections."
            " The underlying cause of scaling needs to be determined through a thorough evaluation by a dermatologist or healthcare professional. Treatment options for scaling depend on the specific condition and may involve moisturizers, topical medications, or systemic therapies, as appropriate.")

        # Header 3
    st.subheader("3. Definite Borders")
    # Paragraph under Header 3
    st.write("When referring to definite borders related to the skin, it typically describes the well-defined edges or margins of a skin lesion or abnormality."
            " Having definite borders means that the boundary between the affected area and the surrounding healthy skin is clear and easily distinguishable."
            " This characteristic can provide important information for clinicians when assessing skin conditions."
            " Here are a few examples where definite borders may be observed: Benign moles, Dermatofibromas, Eczema, Ringworm (tinea corporis).")
    st.write("While definite borders can be a characteristic of benign or non-threatening skin conditions, it is important to note that not all skin abnormalities"
            " with definite borders are harmless. Some malignant or cancerous skin lesions, such as melanoma or basal cell carcinoma, can also exhibit well-defined edges."
            " Therefore, it is essential to consult a dermatologist or healthcare professional for a proper evaluation and diagnosis of any concerning skin lesions,"
            " regardless of their border appearance.")

    # Header 4
    st.subheader("4. Itching")
    # Paragraph under Header 4
    st.write("Itching, also known as pruritus, is a common symptom related to the skin that causes a sensation that prompts a desire to scratch or rub the affected area."
            " Itching can be a bothersome and uncomfortable sensation, and it can occur due to various factors and underlying skin conditions."
            " Here are a few examples: Dry skin, Allergic reactions, Eczema, Psoriasis, Dermatitis, Infections, Urticaria (hives), Systemic conditions.")

    # Header 5
    st.subheader("5. Koebner Phenomenon")
    # Paragraph under Header 5
    st.write("The Koebner phenomenon, also known as isomorphic response or isomorphic phenomenon, is a characteristic skin reaction that occurs in response to physical trauma or injury."
            " Named after Heinrich Koebner, the phenomenon refers to the development of new skin lesions or the recurrence of pre-existing skin lesions at the site of injury or trauma."
            " It is commonly observed in several skin conditions, particularly those with underlying immune-mediated or inflammatory processes."
            " Here are a few examples: Psoriasis, Lichen planus, Vitiligo, Cutaneous lupus erythematosus.")
    st.write("The Koebner phenomenon can occur due to various types of skin trauma, including cuts, burns, surgical incisions, friction, and even minor injuries such as scratches or insect bites."
            " The exact mechanisms underlying this phenomenon are not fully understood, but it is believed to involve the activation of immune cells and the release of inflammatory mediators at the site of injury."
            " It is important to note that not everyone with the mentioned skin conditions will exhibit the Koebner phenomenon, and the occurrence may vary from person to person."
            " If you have a known skin condition or are at risk for developing one, it is advisable to take precautions to avoid skin trauma and seek prompt medical attention if you notice any new or worsening skin lesions at sites of injury.")

    # Header 6
    st.subheader("6. Follicular Papules")
    # Paragraph under Header 6
    st.write("Follicular papules are skin lesions characterized by small, raised bumps or papules that are typically centered around hair follicles."
            " These papules may appear slightly reddened or flesh-colored and can be associated with various skin conditions."
            " Here are some examples: Acne, Folliculitis, Keratosis pilaris, Pityriasis folliculorum, Drug-induced follicular papules.")
    st.write("It is important to note that the presence of follicular papules alone is not enough for a definitive diagnosis."
            " A thorough evaluation by a dermatologist or healthcare professional is necessary to identify the underlying cause and provide appropriate treatment."
            " Additional factors such as the distribution of the papules, associated symptoms, medical history, and sometimes diagnostic tests can aid in making an accurate diagnosis and guiding treatment.")

    # Header 7
    st.subheader("7. Knee and Elbow Involvement")
    # Paragraph under Header 7
    st.write("Knee and elbow involvement in skin disease refers to the presence of skin symptoms or lesions specifically affecting the areas around the knees and elbows."
            " In certain skin conditions, these regions can be particularly prone to developing characteristic rashes, inflammation, or other skin manifestations.")

    # Header 8
    st.subheader("8. Scalp Involvement")
    # Paragraph under Header 8
    st.write("Scalp involvement refers to the presence of skin conditions or diseases that specifically affect the scalp."
            " The scalp is the area of skin covering the top of the head, and it can be affected by various conditions that may cause symptoms such as itching, redness, flaking, hair loss, or the formation of lesions."
            " Here are some examples of skin diseases that commonly involve the scalp: Scalp psoriasis, Seborrheic dermatitis, Tinea capitis, Folliculitis, Alopecia areata.")

    # Header 9
    st.subheader("9. Family History")
    # Paragraph under Header 9
    st.write("Family history in skin disease refers to the presence of a particular skin condition or a group of skin conditions within a person's family."
            " It refers to the occurrence of the same or similar skin diseases among blood relatives, such as parents, siblings, grandparents, aunts, uncles, and cousins.")

    # Header 10
    st.subheader("10. Eosinophils in the Infiltrate")
    # Paragraph under Header 10
    st.write("Eosinophils in the infiltrate refer to the presence of eosinophils, a type of white blood cell, within the inflammatory infiltrate of the skin."
            " Eosinophils are often involved in allergic reactions and certain inflammatory conditions. When eosinophils are present in the infiltrate, it can provide important information about the underlying pathology of the skin condition.")
    st.write("The presence of eosinophils in the infiltrate can be associated with several skin conditions, including: Eosinophilic cellulitis (Wells syndrome), Eosinophilic folliculitis, Drug-induced hypersensitivity reactions, Eosinophilic granulomatosis with polyangiitis (EGPA), Parasitic infections.")

    # Header 11
    st.subheader("11. PNL Infiltrate")
    # Paragraph under Header 11
    st.write("Nerve deficit or nerve thickening, without any cutaneous lesions, with a negative skin smear, and no other identifiable pathology."
            " This is commonly known as pure neuritic leprosy (PNL) and is more common in the Indian subcontinent."
            " Pure Neural Leprosy (PNL) is a rare clinical form of leprosy in which patients do not present with the classical skin lesions but have a high burden of the disability associated with the disease."
            " Clinical characteristics and follow-up of patients in PNL are still poorly described in the literature.")

    # Header 12
    st.subheader("12. Fibrosis of the Papillary Dermis")
    # Paragraph under Header 12
    st.write("Fibrosis of the papillary dermis refers to the excessive deposition of fibrous tissue within the papillary dermis, the uppermost layer of the dermis located just beneath the epidermis."
            " Fibrosis is the process of excessive scarring or connective tissue formation, which can occur in various skin conditions and diseases."
            " When fibrosis affects the papillary dermis, it can lead to several clinical manifestations.")
    st.write("Fibrosis of the papillary dermis can be seen in conditions such as: Scleroderma, Dermal fibrosis in chronic dermatitis, Chronic graft-versus-host disease (GVHD), Cutaneous fibrosing disorders.")

    # Header 13
    st.subheader("13. Exocytosis")
    # Paragraph under Header 13
    st.write("Exocytosis is a cellular process in which vesicles within a cell fuse with the cell membrane, releasing their contents into the extracellular space."
            " While exocytosis itself is not typically associated with skin disorders, certain skin conditions involve abnormal exocytosis or disrupted cellular trafficking processes, which can contribute to the development of skin disorders."
            " Here are a few examples: Psoriasis, Atopic dermatitis, Darier's disease, Pemphigus.")

    # Header 14
    st.subheader("14. Acanthosis")
    # Paragraph under Header 14
    st.write("Acanthosis refers to the thickening of the epidermis, which is the outermost layer of the skin."
            " It is a histopathological finding often associated with various skin conditions and underlying systemic diseases."
            " Acanthosis can occur due to a variety of factors, including chronic irritation, inflammation, hormonal changes, or genetic predisposition.")
    st.write("Here are some examples of acanthosis related to specific skin conditions: Acanthosis nigricans, Acanthosis palmaris et plantaris, Acanthosis in dermatosis neglecta, Acanthosis in certain skin infections.")

    # Header 15
    st.subheader("15. Hyperkeratosis")
    # Paragraph under Header 15
    st.write("Hyperkeratosis refers to an abnormal thickening of the outermost layer of the skin, called the stratum corneum."
            " It is a histopathological finding that can occur in various skin conditions and is often associated with chronic irritation or other underlying factors.")
    st.write("Here are some examples of conditions in which hyperkeratosis is commonly observed: Calluses and corns, Psoriasis, Seborrheic keratosis, Actinic keratosis, Ichthyosis.")
    st.write("Hyperkeratosis can also be seen in other skin conditions, such as certain viral warts, eczema, and fungal infections."
            " It is important to note that hyperkeratosis itself is not a specific diagnosis but rather a histopathological finding."
            " The underlying cause of hyperkeratosis needs to be determined through a combination of clinical evaluation, patient history, and sometimes additional investigations."
            " A dermatologist or healthcare professional should be consulted for an accurate diagnosis and appropriate management of any skin condition associated with hyperkeratosis.")

    # Header 16
    st.subheader("16. Parakeratosis")
    # Paragraph under Header 16
    st.write("Parakeratosis is a specific type of hyperkeratosis that involves the retention of nuclei within the keratinocytes of the stratum corneum, which is the outermost layer of the skin."
            " Unlike the normal process of keratinization, where the nuclei are lost as cells mature and move to the outermost layer, parakeratosis occurs when these nuclei are retained.")

    st.write(" Parakeratosis is commonly seen in certain skin conditions, including: Psoriasis, Pityriasis rubrapilaris, Chronic dermatitis. Parakeratosis can also be present in other skin conditions and histopathological findings, including certain types of viral infections, seborrheic dermatitis, and various disorders affecting keratinization and epidermal differentiation.")
    st.write("It's important to note that parakeratosis is a histopathological observation and, by itself, does not provide a definitive diagnosis. The underlying cause of parakeratosis needs to be evaluatedin conjunction with other clinical findings and may require additional investigations or consultationwith a dermatologist or healthcare professional for an accurate diagnosis and appropriate management.")
        # Header 17
    st.subheader("17. Elongation of the Rete Ridges")
    # Paragraph under Header 17
    st.write("Elongation of the rete ridges, without the presence of clubbing, is a histopathological finding that can be associated with various skin conditions."
            " The rete ridges are the downward projections of the epidermis into the underlying dermis."
            " Elongation of the rete ridges refers to an increase in the length or depth of these projections."
            " Here are some examples of skin conditions where elongation of the rete ridges can be observed: Psoriasis, Lichen planus, Dermatofibroma, Certain types of dermatitis.")

    # Header 18
    st.subheader("18. Spongiform Pustule")
    # Paragraph under Header 18
    st.write("Spongiform pustule is a histopathological finding that can be associated with various skin conditions, particularly those that involve inflammatory reactions in the skin."
            " It refers to the presence of pustules or vesicles filled with inflammatory cells within the epidermis."
            " The term 'spongiform' describes the appearance of the epidermis, which appears spongy due to the presence of these pustules."
            " Here are a few examples of skin conditions where spongiform pustules may be observed: Pustular psoriasis, Acute contact dermatitis, Dyshidrotic eczema, Allergic contact dermatitis.")

    # Header 19
    st.subheader("19. Munro Microabscess")
    # Paragraph under Header 19
    st.write("Munro microabscess is a histopathological finding that is associated with certain skin conditions, particularly those characterized by inflammation and neutrophilic infiltration."
            " It refers to the presence of small collections of neutrophils within the epidermis."
            " These microabscesses are typically observed in the stratum corneum, the outermost layer of the epidermis."
            " The term 'Munro' refers to the scientist who first described these microabscesses."
            " Munro microabscesses are commonly seen in the following skin conditions: Psoriasis, Pustular psoriasis, Acute dermatitis.")

    # Header 20
    st.subheader("20. Disappearance of the Granular Layer")
    # Paragraph under Header 20
    st.write("The disappearance or loss of the granular layer of the epidermis, known as granular layer vacuolization or granular layer degeneration, can be associated with certain skin conditions."
            " It refers to the thinning or absence of the normal granular layer, which is located between the stratum spinosum and the stratum corneum."
            " Here are a few examples of skin conditions where the disappearance of the granular layer may be observed: Toxic epidermal necrolysis (TEN), Pemphigus vulgaris, Severe forms of eczema, Some types of drug reactions.")

    # Header 21
    st.subheader("21. Spongiosis")
    # Paragraph under Header 21
    st.write("Spongiosis is a histopathological finding in the skin that refers to the presence of intercellular edema or accumulation of fluid within the epidermis."
            " It is characterized by the separation or widening of intercellular spaces between keratinocytes in the epidermis."
            " Spongiosis can be associated with various skin conditions, particularly those that involve inflammation or allergic reactions."
            " Here are a few examples: Contact dermatitis, Atopic dermatitis, Allergic reactions, Eczematous dermatoses")

    # Header 22
    st.subheader("22. Inflammatory Mononuclear Infiltrate")
    # Paragraph under Header 22
    st.write("An inflammatory mononuclear infiltrate is a histopathological finding related to the skin that refers to the presence of inflammatory cells composed primarily of mononuclear cells, such as lymphocytes and monocytes/macrophages, in the affected tissue."
            " This type of infiltrate is commonly observed in various skin conditions, indicating an immune response or inflammation."
            " Here are a few examples of skin conditions where an inflammatory mononuclear infiltrate may be observed: Dermatitis, Autoimmune skin diseases, Infections, Granulomatous skin diseases.")

    # Disclaimer and Limitations
    st.subheader("Disclaimer:")
    st.write("The predictive model developed and evaluated using the provided dataset and attributes is intended solely for research and informational purposes."
            " While the model may have achieved a high F1 score, it is important to understand its limitations and exercise caution when interpreting its results."
            " The model's predictions are based on historical data and patterns present in the dataset, and its accuracy may vary when applied to new, unseen data.")
    st.header("Limitations:")
    st.write("1. Domain-Specific: The model is specifically designed to predict erythemato-squamous skin diseases within the scope of the provided attributes."
            " It may not generalize well to other types of skin disorders or medical conditions beyond the dataset's scope.")
    st.write("2. Data Quality: The performance of the model heavily relies on the quality and representativeness of the data it was trained on."
            " Any errors, biases, or missing information in the dataset could impact the model's accuracy and reliability.")
    st.write("3. Changing Medical Landscape: Medical knowledge and practices are constantly evolving. The model's accuracy might be affected by changes in diagnostic criteria, treatment methods, and disease prevalence that have occurred after the dataset was collected.")
    st.write("4. Biases and Ethical Considerations: The dataset and model might inadvertently reflect biases present in the data collection process or societal factors. It's essential to consider ethical implications when using the model in a real-world medical context.")
    st.write("5. Limited Features: The model's predictions are based on a subset of clinical and histopathological attributes. Other factors, such as genetic information, patient history, or environmental factors, may play a significant role in accurate disease diagnosis but are not considered in this model.")
    st.write("6. No Patient Identifiers: The dataset lacks patient identifiers, making it impossible to track individual patients over time or verify the accuracy of family history information.")
    st.write("7. Clinical Consultation: The model's predictions should not replace professional medical judgment. Physicians and dermatologists should make final diagnoses based on a combination of clinical assessment, patient history, and additional medical tests.")
    st.write("In summary, while the Gradient Boosting model has shown a promising F1 score on the provided dataset, it is crucial to understand its limitations and exercise caution when applying its predictions in real-world medical scenarios."
            " Rigorous validation, ongoing monitoring, and collaboration with medical professionals are essential steps before considering deployment for practical use.")

if __name__ == "__main__":
    main()

    