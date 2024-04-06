class ContentRetrievalError(Exception):
    """Exceção para falhas ao obter conteúdo da página."""
    pass

class TableNotFoundError(Exception):
    """Exceção para quando a tabela com ID 'stocks' não é encontrada."""
    pass

class StrongTagsNotFoundError(Exception):
    """Exceção para quando as tags 'strong' não são encontradas."""
    pass

class TextTagsNotFoundError(Exception):
    """Exceção para quando o texto das tags 'a' não é encontrado."""
    pass