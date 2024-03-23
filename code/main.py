from classification import *
from siamese_network import *
from tensorflow.keras.models import load_model

if __name__ == "__main__":
    only_variant = False
    data_encoded = False
    classification = True
    siamese_net = True
    siamese_variants = True

    ####################################################################################################################
    # DATA
    dataset_path = ("dataset/data_mrna/SNP_DEL_INS_CNA_mutations_and_variants/"
                    "data_mrna_v2_seq_rsem_trasposto_normalizzato_deviazione_0030_dataPatient_mutations_and_variants.csv")

    encoded_path = "models/0030/classification/espressione_genomica_con_varianti_2LAYER/encoded-dataset.csv"

    ####################################################################################################################

    # CLASSIFICATION
    model_path = "models/0030/classification/espressione_genomica_con_varianti_2LAYER/"

    risultati_classification = ("risultati/classification/0030/"
                                "classification_espressione_genomica_con_varianti_2LAYER.csv")

    ####################################################################################################################

    # SIAMESE
    siamese_path = "models/0030/siamese/espressione_genomica_con_varianti_2LAYER/"

    risultati_siamese = "risultati/siamese/0030/siamese_espressione_genomica_con_varianti_2LAYER.txt"

    ####################################################################################################################

    encoded_data, dataset_df, weights, n_classes, classes, le, y = (
        pre_processing(dataset_path, encoded_path, data_encoded, only_variant))

    if classification:
        model = classification_model(model_path, risultati_classification,
                                     encoded_data, weights, n_classes, classes, le, y)

    if siamese_net:
        if not classification:
            model = load_model(model_path + "model.keras", custom_objects={'loss': weighted_categorical_crossentropy})

        genes_len = dataset_df.shape[1]
        input_shape = (genes_len, 1)

        cancer_type = pd.DataFrame(y, columns=['CANCER_TYPE'])
        siamese_network(siamese_path, risultati_siamese, dataset_df, model,
                        input_shape, genes_len, cancer_type, siamese_variants)
