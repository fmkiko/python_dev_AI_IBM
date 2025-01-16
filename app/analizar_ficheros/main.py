import pandas as pd
import os

def convert_xls_to_csv(xls_file, csv_file):
    """
    Convierte un archivo .xls a .csv

    Parameters:
        xls_file (str): Ruta del archivo .xls de entrada
        csv_file (str): Ruta del archivo .csv de salida
    """
    try:
        # Leer archivo .xls
        data = pd.read_excel(xls_file, engine='xlrd', header=3)
        # Guardar como .csv
        data.to_csv(csv_file, index=False)
        print(f"Archivo convertido y guardado como: {csv_file}")
    except Exception as e:
        print(f"Error al convertir el archivo: {e}")

def load_csv_to_dataframe(csv_file):
    """
    Carga un archivo .csv en un DataFrame de pandas

    Parameters:
        csv_file (str): Ruta del archivo .csv

    Returns:
        DataFrame: DataFrame con los datos del archivo .csv
    """
    try:
        df = pd.read_csv(csv_file)
        print(df.head())
        print("Archivo cargado exitosamente en un DataFrame.")
        return df
    except Exception as e:
        print(f"Error al cargar el archivo .csv: {e}")
        return None

def filter_dataframe_columns(df, columns):
    """
    Filtra columnas específicas de un DataFrame

    Parameters:
        df (DataFrame): DataFrame de entrada
        columns (list): Lista de columnas a seleccionar

    Returns:
        DataFrame: DataFrame filtrado
    """
    try:
        filtered_df = df[columns]
        print("Columnas seleccionadas correctamente.")
        return filtered_df
    except KeyError as e:
        print(f"Error: Una o más columnas no existen en el DataFrame. {e}")
        return None

# Ejecución principal
if __name__ == "__main__":
    print("Programa para convertir .xls a .csv y realizar consultas en un DataFrame.")

    # Solicitar rutas
    path_xls = "./ficheros/xls/TT221124.139_2021.XLS"
    xls_file = path_xls 
    csv_file = "./ficheros/csv/TT221124.139_2021.csv"

    # Convertir el archivo
    convert_xls_to_csv(xls_file, csv_file)

    # Cargar el archivo CSV en un DataFrame
    df = load_csv_to_dataframe(csv_file)

    if df is not None:
        print("\nColumnas disponibles:")
        print(df.columns.tolist())

        # Filtrar filas que tienen valor en la columna "Ingreso (+)"
        df = df.dropna(subset=["Ingreso (+)"])

        # Seleccionar columnas para consulta
        columns = ["F. Operación","Ingreso (+)", "Concepto complementario 1",  ] #input("Ingrese las columnas a seleccionar (separadas por comas): ").split(",")
        columns = [col.strip() for col in columns]  # Eliminar espacios extra

        filtered_df = filter_dataframe_columns(df, columns)
        print(filtered_df.head(10))

        if filtered_df is not None:
            print("\nDatos filtrados:")
            print(filtered_df)

            # Guardar DataFrame filtrado en un nuevo archivo CSV si se desea
            save_filtered = input("\u00bfDesea guardar los datos filtrados en un nuevo archivo .csv? (s/n): ").lower()
            if save_filtered == 's':
                nombre_archivo = input("Ingrese el nombre del archivo: ")
                filtered_csv_file = "./ficheros/transformer_csv/" + nombre_archivo #input("Ingrese la ruta para guardar el archivo filtrado: ")
                filtered_df.to_csv(filtered_csv_file, index=False)
                print(f"Datos filtrados guardados en: {filtered_csv_file}")
