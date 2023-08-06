
## Либка для получения доступа к ресурсам spt

Один раз инициализируете фабрику и потом с помощью методов `get_<recource_name>`(получить креды `get_<recource_name>_credentials`) получаете наобходимый доступ без прописывания всех логинов, явок, паролей

Реализованные ресурсы на текущий момент:

- Доступы к базам
- S3Manager по умолчанию подключается к aws s3 storage. 
- DataVault
- ModelManager
- ModelStorage

## Пример использования
В дс фабрику нужно передать обычную фабрику, что полного использования функционала

Фабрика позволяет получить доступ к `ModelManager` & `PipelineManager`, которые являются singleton'ами

```python
...
spt_factory_resource = MongoFactory(
    mongo_url=os.getenv('MONGO_URL'),
    tlsCAFile=os.getenv('SSLROOT'),
)
spt_ds = DsFactory(spt_factory_resource)
model_manager_1 = spt_ds.get_model_manager()
# Вернет один и тот же объект
model_manager_1 = spt_ds.get_model_manager()
model_manager_2 = spt_ds.get_model_manager()

# Вернет один и тот же объект
pipeline_manager_1 = spt_ds.get_pipeline_manager()
pipeline_manager_2 = spt_ds.get_pipeline_manager()
```

## Работа с rest моделями

В данном блоке будет описано как получить объект типа RestModel, который оборачивает работу с rest моделями

### Prerequirements

Прежде чем начать пользоваться rest моделью вам необходимо, чтобы она была задеплоина как rest-service, для этого необходимо:

 - Провести исследование и обучить/найти подходящую модель
 - Сохранить ее с помощью mlflow.sklearn.log_mode mlflow.pyfunc.log_mode etc в наш mlflow, важно чтобы она была зарегистрирована (про это подробнее см. wiki) 
 - Написать Dockerfile, оборачивающий модель в docker (про это подробнее см. wiki) 
 - Когда вы уверены, что модель прекрасна - перевести ее в ui mlflow в production версию
 - Отдать Dockerfiles DevOps, который будет их разворачивать
 - Попросить кого-то из DevOps задеплоить
 - Проверить что rest модель отвечает

### Получение предсказания из rest модели

Подход 1 (Получение модели напрямую из имени)

```python
import os
from spt_factory import MongoFactory
from spt_datascience.factory import DsFactory
from spt_datascience.datascience.model_manager import ModelManager


if __name__ == '__main__':

    spt_factory_resource = MongoFactory(
        mongo_url=os.getenv('MONGO_URL'),
        tlsCAFile=os.getenv('SSLROOT'),
    )
    spt_ds = DsFactory(spt_factory_resource)
    model_manager: ModelManager = spt_ds.get_model_manager()

    # модель доступна по пути https://api.models.common.smartpredictiontech.ru/model1-cpu/invocations
    rest_model = model_manager.get_rest_model("model1-cpu")

    print(rest_model.predict(['Привет мир!', 'Как дела?']))

```

Подход 2 (С использованием конфигурации модели в mongo)

В данном случае требуется добавить model_config в mongo следующего шаблона

```json
{
    ...
    "storage_type": "rest"
    "name": <model_name from url>
    "model_package" : "spt_datascience.datascience.models.rest_model",
    "model_class" : "RestModel",
    "bins": {}
    ...
} 
```
 
Код получения объекта модели и предсказания:

```python
import os
from spt_factory import MongoFactory
from spt_datascience.factory import DsFactory
from spt_datascience.datascience.model_manager import ModelManager


if __name__ == '__main__':

    spt_factory_resource = MongoFactory(
        mongo_url=os.getenv('MONGO_URL'),
        tlsCAFile=os.getenv('SSLROOT'),
    )
    spt_ds = DsFactory(spt_factory_resource)
    model_manager: ModelManager = spt_ds.get_model_manager()

    # в mongo лежит конфиг модели, у которого name совпадает с <name> в url модели
    # https://api.models.common.smartpredictiontech.ru/<name>/invocations
    rest_model = model_manager.get_model(model_id="rest/tfidf_lr_pipeline_37212_potok/test")

    print(rest_model.predict(['Привет мир!', 'Как дела?']))
```