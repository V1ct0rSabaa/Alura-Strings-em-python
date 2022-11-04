class Extrator_url:
    def __init__(self, url: str) -> None:
        self._url = url.strip()
        self.validar_url()
        self._base_url: str = self._url[self._url.find("?"):]
    
    def validar_url(self):
        if len(self._url) == 0:
            raise ValueError("Erro, a URL está vazia")
        
    @property
    def base_url(self) -> str:
        return self._base_url
    
    def get_valor_parametro(self, valor_parametro: str) -> str:
        indice_parametro: int = self._base_url.find(valor_parametro)
        indice_valor: int = indice_parametro + len(valor_parametro) + 1
        valor: str = self._base_url[indice_valor: 
            self._base_url.find("&") if "&" in valor_parametro else len(valor_parametro)]
        return valor
    
    def __len__(self) -> int:
        return len(self._url)
        
    def __str__(self) -> str:
        return self._url