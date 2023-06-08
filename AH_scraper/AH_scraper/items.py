# Define here the models for your scraped items
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ChocolateItem(scrapy.Item):
    product_id = scrapy.Field()
    product_naam = scrapy.Field()
    prijs = scrapy.Field()
    kilo_prijs = scrapy.Field()
    omschrijving = scrapy.Field()
    inhoud = scrapy.Field()
    ingredienten = scrapy.Field()
    kenmerken = scrapy.Field()
    allergie_bevat = scrapy.Field()
    allergie_kan_bevatten = scrapy.Field()
    leverancier = scrapy.Field()
    adres_leverancier = scrapy.Field()
    product_url = scrapy.Field()

    # fields to export
    fields_to_export = ['product_id','product_naam', 'prijs', 'kilo_prijs', 'omschrijving', 'inhoud', 'ingredienten',
     'kenmerken', 'allergie_bevat', 'allergie_kan_bevatten', 'leverancier', 'adres_leverancier', 'product_url']