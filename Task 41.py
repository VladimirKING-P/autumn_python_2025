#todo: Создайте иерархию классов для экспорта данных в разные форматы.
# Требования:
# Абстрактный базовый класс DataExporter:
# Методы:
# export(self, data) - абстрактный метод
# get_format_name(self) - возвращает название формата
# validate_data(self, data) - общий метод проверки данных (не пустые ли)
# Конкретные реализации:
# JSONExporter:
# Экспортирует данные в JSON-формат
# Добавляет поле "export_timestamp" с текущим временем
# CSVExporter:
# Экспортирует данные в CSV (если data - список словарей)
# Автоматически определяет заголовки из ключей первого элемента
# XMLExporter:
# Создает XML структуру с корневым элементом <report>
# HTMLExporter (дополнительно):
# Создает красивую HTML-таблицу с CSS-стилями

from abc import ABC, abstractmethod
import json
import csv
from datetime import datetime
from typing import Any, Optional, List, Dict
import xml.etree.ElementTree as ET
from xml.dom import minidom
from io import StringIO




class DataExporter(ABC):
    @abstractmethod
    def export(self, data: Any) -> None:
        """Абстрактный метод экспорта данных."""
        pass

    def get_format_name(self) -> str:
        """Возвращает название формата (из имени класса)."""
        return self.__class__.__name__.replace('Exporter', '')

    def validate_data(self, data: Any) -> bool:
        """Проверяет, что данные не пустые."""
        if data is None:
            raise ValueError("Данные не могут быть None")
        if isinstance(data, (list, dict)) and len(data) == 0:
            raise ValueError("Данные пусты")
        return True



class JSONExporter(DataExporter):
    def __init__(self, indent: int = 2, ensure_ascii: bool = False):
        self.indent = indent
        self.ensure_ascii = ensure_ascii

    def export(self, data: Any) -> None:
        self.validate_data(data)
        exported_data = {
            "data": data,
            "export_timestamp": datetime.now().isoformat()
        }
        json_str = json.dumps(
            exported_data,
            ensure_ascii=self.ensure_ascii,
            indent=self.indent
        )
        print(json_str)



class CSVExporter(DataExporter):
    def __init__(
        self,
        delimiter: str = ',',
        lineterminator: str = '\n',
        quoting: int = csv.QUOTE_MINIMAL
    ):
        self.delimiter = delimiter
        self.lineterminator = lineterminator
        self.quoting = quoting

    def export(self, data: Any) -> None:
        self.validate_data(data)

        if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
            raise ValueError("Для CSV данные должны быть списком словарей")

        if len(data) == 0:
            print("Нет данных для экспорта")
            return

        # Собираем все возможные ключи
        all_keys = set()
        for item in data:
            all_keys.update(item.keys())
        fieldnames = sorted(all_keys)

        output = StringIO()
        writer = csv.DictWriter(
            output,
            fieldnames=fieldnames,
            delimiter=self.delimiter,
            lineterminator=self.lineterminator,
            quoting=self.quoting
        )

        writer.writeheader()
        for row in data:
            writer.writerow({k: row.get(k, '') for k in fieldnames})

        print(output.getvalue().strip())
        output.close()



class XMLExporter(DataExporter):
    def __init__(self, root_tag: str = "report", indent: str = "  "):
        self.root_tag = root_tag
        self.indent = indent

    def export(self, data: Any) -> None:
        self.validate_data(data)

        root = ET.Element(self.root_tag)
        root.set("export_timestamp", datetime.now().isoformat())

        for item in data:
            record = ET.SubElement(root, "record")
            for key, value in item.items():
                child = ET.SubElement(record, key)
                child.text = str(value)

        rough_string = ET.tostring(root, 'unicode')
        reparsed = minidom.parseString(rough_string)
        pretty_xml = reparsed.toprettyxml(indent=self.indent)


        lines = [
            line for line in pretty_xml.splitlines()
            if not line.strip().startswith('<?xml')
        ]
        print('\n'.join(lines))




class HTMLExporter(DataExporter):
    def __init__(
        self,
        title: str = "Отчёт",
        css: Optional[str] = None
    ):
        self.title = title
        self.css = css or """
        <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 12px; text-align: left; }
        th { background-color: #f2f2f2; font-weight: bold; }
        tr:nth-child(even) { background-color: #f9f9f9; }
        .timestamp { color: #666; font-size: 0.9em; margin: 15px 0; }
        h2 { color: #333; margin-bottom: 5px; }
        </style>
        """

    def export(self, data: Any) -> None:
        self.validate_data(data)

        headers = sorted(data[0].keys()) if data else []
        header_row = "".join(f"<th>{header}</th>" for header in headers)
        rows = ""

        for item in data:
            row = "".join(
                f"<td>{item.get(key, '')}</td>" for key in headers
            )
            rows += f"<tr>{row}</tr>"

        html = f"""
        <html>
        <head>{self.css}</head>
        <body>
          <h2>{self.title}</h2>
          <p class="timestamp">Экспортировано: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
          <table>
            <thead><tr>{header_row}</tr></thead>
            <tbody>{rows}</tbody>
          </table>
        </body>
        </html>
        """
        print(html)



# Пример использования
if __name__ == "__main__":
    sales_data = [
        {"product": "Laptop", "price": 1000, "quantity": 2},
        {"product": "Mouse", "price": 50, "quantity": 10}
    ]

    exporters = [
        JSONExporter(indent=4),
        CSVExporter(delimiter=';'),
        XMLExporter(root_tag="sales_report"),
        HTMLExporter(title="Продажи товаров")
    ]

    for exporter in exporters:
        print(f"Формат: {exporter.get_format_name()}")
        exporter.export(sales_data)
        print("---")

# на втором цикле происходит ошибка в sales_data, как можно исправить