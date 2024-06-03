from flask_sqlalchemy import Pagination

from temp.dto import DTO


class PaginationDTO(DTO):
    def __init__(self, page, exclude_columns=[]):
        if not isinstance(page, Pagination):
            raise ValueError

        self._page = page.page
        self._pages = page.pages
        self._per_page = page.per_page
        self._total_all = page.total
        self._exclude_columns = ['query', 'query_class', 'metadata', 'registry']
        self._exclude_columns.extend(exclude_columns)
        def item_convert_iter(items):
            for item in items:
                yield {_: getattr(item, _) for _ in dir(item) if
                       not _.startswith('_') and _ not in self._exclude_columns}

        self._values = [_ for _ in item_convert_iter(page.items)]
    def to_json(self):
        return {
            "page": self._page,
            "pageCount": self._pages,
            "pageSize": self._per_page,
            "itemCount": self._total_all,
            "list": self._values
        }
