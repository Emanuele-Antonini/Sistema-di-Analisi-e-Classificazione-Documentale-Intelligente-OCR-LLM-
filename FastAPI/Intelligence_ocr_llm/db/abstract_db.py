import abc

class AbstractRepository(abc.ABC):
    
    @abc.abstractmethod
    async def add(self, document: dict):
        raise NotImplementedError

    @abc.abstractmethod
    async def get(self, query: dict) -> dict:
        raise NotImplementedError
        
    @abc.abstractmethod
    async def update(self, query: dict, update_data: dict):
        raise NotImplementedError