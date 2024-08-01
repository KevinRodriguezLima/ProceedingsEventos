from models.documentos.Documento import Documento

class FabricaDocumento:
    def __init__(self):
        return
        
    def crear_documento(self, resumen, datos, conclusion, num_pag, evento_id):
        documento = Documento(
            resumen=resumen,
            datos=datos,
            conclusion=conclusion,
            num_pag=num_pag,
            evento_id=evento_id,
            autores="Autor Desconocido"  
            )
        return documento
