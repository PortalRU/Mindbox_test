from pyspark.sql import DataFrame

def get_product_category_pairs(
  products: DataFrame,
  categories: DataFrame,
  products_category_links: DataFrame
) -> DataFrame:
  '''
  Возвращает датафрейм со всеми парами "Имя продукта - Имя категории" и продуктам без категорий.

  Параметры:
    - products: датафрейм с продуктами (должен содержать колонки 'id' и 'name')
    - categories: датафрейм с категориями (должен содержать колонки 'id' и 'name')
    - product_category_links: датафрейм с связями продукт-категория 
                               (должен содержать колонки 'left_id' и 'right_id')
    
  Возвращает:
    - Датафрейм с колонками ['product.name', 'category.name'], где category.name может быть NULL
  '''
  result = products \
    .join(
      products_category_links,
      products_category_links['left_id'] == products['id'],
      how='left'
    ) \
    .join(
      categories,
      categories['id'] == products_category_links['right_id'],
      how='left'
    ) \
    .select(
      products['name'].alias('product_name'),
      categories['name'].alias('category_name')
    ) \
    .filter(
      (categories['name'].isNotNull()) |
      (categories['id'].isNull()) 
    ) \
    .sort(
      categories['name']
    )

  return result
