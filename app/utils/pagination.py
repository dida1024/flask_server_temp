from typing import List, Dict


class Pagination:
    def __init__(self, items: List[dict], total: int, page: int, per_page: int):
        self.items = items
        self.total = total
        self.page = page
        self.per_page = per_page

    @property
    def pages(self) -> int:
        """计算总页数"""
        return (self.total + self.per_page - 1) // self.per_page  # 向上取整

    def to_dict(self) -> Dict[str, any]:
        """将分页信息转换为字典"""
        return {
            "total": self.total,
            "page": self.page,
            "per_page": self.per_page,
            "pages": self.pages,
            "items": self.items
        }
