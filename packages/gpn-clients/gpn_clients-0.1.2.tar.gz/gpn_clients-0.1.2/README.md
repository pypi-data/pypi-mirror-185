# 🀣 🅖🅟🅝 🅲🅻🅸🅴🅽🆃🆂 🀣

![Code Coverage](https://img.shields.io/badge/Coverage-90%25-green.svg)

ГПН Клиенты предоставляющие интерфейс для работы с источниками данных.

## Базовое использование

**Конфигурация** клиента на примере клиента NSI:

```python
from gpn_clients.core.config import nsi_config


NSI_HOST: str = "https://test-nsi-host-228.com"
NSI_PORT: int = 443

# Конфигурация клиента
nsi_config.set_config(
    host=NSI_HOST,
    port=NSI_PORT,
)
```

После конфигурации клиента можно использовать его методы.
Использование интерфейсов NSI **Алгоритмов**:

```python
from pydantic import HttpUrl

from gpn_clients.clients.nsi.v1.algorithms import (
    AbstractAlgorithms,
    NSIAlgorithms,
)


nsi_algorithms: AbstractAlgorithms = NSIAlgorithms()

# Получение URL для списка алгоритмов
algorithms: HttpUrl = nsi_algorithms.get_all()

# Получение URL для алгоритма по его ID
algorithm: HttpUrl = nsi_algorithms.get_by_id(algorithm_id=1)
```
