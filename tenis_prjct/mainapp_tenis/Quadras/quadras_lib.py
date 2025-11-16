import json
from pathlib import Path

# mainapp_tenis/quadras_data.json
DATA_PATH = Path(__file__).resolve().parent.parent / "quadras_data.json"  # ou "quadras.json" se for esse o nome

def load_quadras():
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return -1001  # arquivo não encontrado
    
def salvar_quadras(quadras_list):
    try:
        with open(DATA_PATH, "w", encoding="utf-8") as file:
            json.dump(quadras_list, file, indent=4, ensure_ascii=False)
            return 0  # sucesso
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")
        return -1002  # erro ao salvar o arquivo

def get_quadra_by_id(quadra_id, todas_quadras):

    print("\nTodas as quadras que estou consultando:\n\n")
    print(todas_quadras)

    # Garantir que o JSON foi carregado corretamente
    if isinstance(todas_quadras, int):
        print("Erro ao carregar quadras (retornou código de erro).")
        return None

    # Percorre cada quadra do JSON
    for quadra in todas_quadras:
        # Se o campo "Id" bater com o ID procurado
        print(f"\nNome Quadra: {quadra["Nome"]}\n")

        print(f"\n quadra.get('ID'): {quadra.get("Id")} == quadra_id: {quadra_id}\n")

        if quadra.get("Id") == quadra_id:
            return quadra  # Retorna
        
    return -1 #quadra não encontrada