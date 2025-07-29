import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/letscrape-6bRBa3QguO5/api/local-business-data'

mcp = FastMCP('local-business-data')

@mcp.tool()
def search(query: Annotated[str, Field(description='Search query / keyword Examples: Plumbers near New-York, USA Bars in 94102, USA')],
           limit: Annotated[Union[int, float, None], Field(description='Maximum number of businesses to return. Default: 20 Allowed values: 1-500 Default: 20')] = None,
           lat: Annotated[Union[int, float, None], Field(description='Latitude of the coordinates point from which the query is applied - recommended to use so that results are biased towards this location. Defaults to some central location in the region (see the region parameter). Default: 37.359428')] = None,
           lng: Annotated[Union[int, float, None], Field(description='Longitude of the coordinates point from which the query is applied - recommended to use so that results are biased towards this location. Defaults to some central location in the region (see the region parameter). Default: -121.925337')] = None,
           zoom: Annotated[Union[str, None], Field(description='Zoom level on which to make the search (the viewport is determined by lat, lng and zoom). Default: 13')] = None,
           language: Annotated[Union[str, None], Field(description='Set the language of the results. For a list of supported language codes see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes . Default: en')] = None,
           region: Annotated[Union[str, None], Field(description='Query Google Maps from a particular region or country. For a list of supported region/country codes see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes (Alpha-2 code). Default: us')] = None,
           subtypes: Annotated[Union[str, None], Field(description='Find businesses with specific subtypes, specified as a comma separated list of types (business categories). For the complete list of types, see https://daltonluka.com/blog/google-my-business-categories. Examples: Plumber,Carpenter,Electrician Night club,Dance club,Bar,Pub')] = None,
           verified: Annotated[Union[bool, None], Field(description='Only return verified businesses')] = None,
           business_status: Annotated[Union[str, None], Field(description='Find businesses with specific status, specified as a comma separated list of the following values: OPEN, CLOSED_TEMPORARILY, CLOSED. Examples: OPEN CLOSED_TEMPORARILY,CLOSED')] = None,
           extract_emails_and_contacts: Annotated[Union[bool, None], Field(description='Extract emails, contacts and social profiles for each business in the response. In case true, businesses will be enriched with a emails_and_contacts field with emails, phones, Facebook, LinkedIn, Instagram and other social profiles. Default: false Note: in case true, the endpoint will scrape emails and contacts from the business website (in case non-empty) - For each such business, the API will charge an additional credit.')] = None,
           fields: Annotated[Union[str, None], Field(description='A comma separated list of business fields to include in the response (field projection). By default all fields are returned. Example: business_id,type,phone_number,full_address')] = None) -> dict: 
    '''Search local businesses on Google Maps with an option to pull emails and social profile links from their website (see the `extract_emails_and_contacts` parameter below).'''
    url = 'https://local-business-data.p.rapidapi.com/search'
    headers = {'x-rapidapi-host': 'local-business-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'limit': limit,
        'lat': lat,
        'lng': lng,
        'zoom': zoom,
        'language': language,
        'region': region,
        'subtypes': subtypes,
        'verified': verified,
        'business_status': business_status,
        'extract_emails_and_contacts': extract_emails_and_contacts,
        'fields': fields,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_in_area(query: Annotated[str, Field(description='Search query / keyword')],
                   lat: Annotated[Union[int, float], Field(description='Latitude of the center coordinate point of the area to search in. Default: 37.359428')],
                   lng: Annotated[Union[int, float], Field(description='Longitude of the center coordinate point of the area to search in. Default: -121.925337')],
                   zoom: Annotated[str, Field(description='Zoom level on which to make the search (the search area / viewport is determined by lat, lng and zoom on a 1000x1000 screen).')],
                   limit: Annotated[Union[int, float, None], Field(description='Maximum number of businesses to return. Default: 20 Allowed values: 1-500 Default: 20')] = None,
                   language: Annotated[Union[str, None], Field(description='Set the language of the results. For a list of supported language codes see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes . Default: en')] = None,
                   region: Annotated[Union[str, None], Field(description='Query Google Maps from a particular region or country. For a list of supported region/country codes see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes (Alpha-2 code). Default: us')] = None,
                   subtypes: Annotated[Union[str, None], Field(description='Find businesses with specific subtypes, specified as a comma separated list of types (business categories). For the complete list of types, see https://daltonluka.com/blog/google-my-business-categories. Examples: Plumber,Carpenter,Electrician Night club,Dance club,Bar,Pub')] = None,
                   extract_emails_and_contacts: Annotated[Union[bool, None], Field(description='Extract emails, contacts and social profiles for each business in the response. In case true, businesses will be enriched with a emails_and_contacts field with emails, phones, Facebook, LinkedIn, Instagram and other social profiles. Default: false Note: in case true, the endpoint will scrape emails and contacts from the business website (in case non-empty) - For each such business, the API will charge an additional credit.')] = None,
                   fields: Annotated[Union[str, None], Field(description='A comma separated list of business fields to include in the response (field projection). By default all fields are returned. Example: business_id,type,phone_number,full_address')] = None) -> dict: 
    '''Search businesses in a specific geographic area defined by a center coordinate point and zoom level. To see it in action, make a query on Google Maps, wait for the results to show, move the map or change the zoom and click "Search this area" at the top.'''
    url = 'https://local-business-data.p.rapidapi.com/search-in-area'
    headers = {'x-rapidapi-host': 'local-business-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'lat': lat,
        'lng': lng,
        'zoom': zoom,
        'limit': limit,
        'language': language,
        'region': region,
        'subtypes': subtypes,
        'extract_emails_and_contacts': extract_emails_and_contacts,
        'fields': fields,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_nearby(query: Annotated[str, Field(description='Search query / keyword Examples: Bars and pubs Plumbers')],
                  lat: Annotated[Union[int, float], Field(description='Latitude of the geographic coordinates to search near by. Default: 37.359428')],
                  lng: Annotated[Union[int, float], Field(description='Longitude of the geographic coordinates to search near by. Default: -121.925337')],
                  limit: Annotated[Union[int, float, None], Field(description='Maximum number of businesses to return. Default: 20 Allowed values: 1-500 Default: 20')] = None,
                  language: Annotated[Union[str, None], Field(description='Set the language of the results. For a list of supported language codes see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes . Default: en')] = None,
                  region: Annotated[Union[str, None], Field(description='Query Google Maps from a particular region or country. For a list of supported region/country codes see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes (Alpha-2 code). Default: us')] = None,
                  subtypes: Annotated[Union[str, None], Field(description='Find businesses with specific subtypes, specified as a comma separated list of types (business categories). For the complete list of types, see https://daltonluka.com/blog/google-my-business-categories. Examples: Plumber,Carpenter,Electrician Night club,Dance club,Bar,Pub')] = None,
                  extract_emails_and_contacts: Annotated[Union[bool, None], Field(description='Extract emails, contacts and social profiles for each business in the response. In case true, businesses will be enriched with a emails_and_contacts field with emails, phones, Facebook, LinkedIn, Instagram and other social profiles. Default: false Note: in case true, the endpoint will scrape emails and contacts from the business website (in case non-empty) - For each such business, the API will charge an additional credit.')] = None,
                  fields: Annotated[Union[str, None], Field(description='A comma separated list of business fields to include in the response (field projection). By default all fields are returned. Example: business_id,type,phone_number,full_address')] = None) -> dict: 
    '''Search businesses near by specific geographic coordinates. To see it in action, right click on a specific point in the map on Google Maps and select "Search nearby", enter a query and search.'''
    url = 'https://local-business-data.p.rapidapi.com/search-nearby'
    headers = {'x-rapidapi-host': 'local-business-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'lat': lat,
        'lng': lng,
        'limit': limit,
        'language': language,
        'region': region,
        'subtypes': subtypes,
        'extract_emails_and_contacts': extract_emails_and_contacts,
        'fields': fields,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def business_details(business_id: Annotated[str, Field(description='Unique Business Id. Accepts google_id / business_id or place_id. Examples: 0x880fd393d427a591:0x8cba02d713a995ed ChIJkaUn1JPTD4gR7ZWpE9cCuow In addition, batching of up to 20 Business Ids is supported in a single request using a comma separated list (e.g. business_id=id1,id2).')],
                     extract_emails_and_contacts: Annotated[Union[bool, None], Field(description='Whether to extract emails, contacts and social profiles for the business. In case true, businesses will be enriched with a emails_and_contacts field, potentially containing emails, phones, Facebook, LinkedIn, Instagram and other social profiles. Default: true')] = None,
                     extract_share_link: Annotated[Union[bool, None], Field(description="Whether to extract place's share link for the business. In case true, businesses will be enriched with a share_link field containing a shortened Google URL for sharing (e.g. https://goo.gl/maps/oxndE8SVaNU5CV6p6). Default: false")] = None,
                     fields: Annotated[Union[str, None], Field(description='A comma separated list of business fields to include in the response (field projection). By default all fields are returned. Example: business_id,type,phone_number,full_address')] = None,
                     region: Annotated[Union[str, None], Field(description='Query Google Maps from a particular region or country. For a list of supported region/country codes see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes (Alpha-2 code). Default: us')] = None,
                     language: Annotated[Union[str, None], Field(description='Set the language of the results. For a list of supported language codes see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes . Default: en')] = None,
                     coordinates: Annotated[Union[str, None], Field(description='Geographic coordinates of the location from which the query is applied - recommended to use so that results are biased towards this location. Defaults to some central location in the region (see the region parameter).')] = None) -> dict: 
    '''Get full business details including emails and social contacts. Supports batching of up to 20 Business Ids.'''
    url = 'https://local-business-data.p.rapidapi.com/business-details'
    headers = {'x-rapidapi-host': 'local-business-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'business_id': business_id,
        'extract_emails_and_contacts': extract_emails_and_contacts,
        'extract_share_link': extract_share_link,
        'fields': fields,
        'region': region,
        'language': language,
        'coordinates': coordinates,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def business_reviews(business_id: Annotated[str, Field(description='Unique Business Id. Accepts google_id / business_id or place_id. Examples: 0x880fd393d427a591:0x8cba02d713a995ed ChIJkaUn1JPTD4gR7ZWpE9cCuow')],
                     limit: Annotated[Union[int, float, None], Field(description='Maximum number of business reviews to return. Default: 20 Allowed values: 1-1000 Default: 5')] = None,
                     offset: Annotated[Union[int, float, None], Field(description='Number of business reviews to skip (for pagination/scrolling). Default: 0 Default: 0')] = None,
                     translate_reviews: Annotated[Union[bool, None], Field(description='Whether to translate reviews to the language specified as the language parameter (defaults to false).')] = None,
                     query: Annotated[Union[str, None], Field(description='Return reviews matching a text query.')] = None,
                     sort_by: Annotated[Literal['most_relevant', 'newest', 'highest_ranking', 'lowest_ranking', None], Field(description='How to sort the reviews in the results. Default: most_relevant Allowed values: most_relevant, newest, highest_ranking, lowest_ranking')] = None,
                     fields: Annotated[Union[str, None], Field(description='A comma separated list of review fields to include in the response (field projection). By default all fields are returned. Example: review_id,review_text,rating')] = None,
                     region: Annotated[Union[str, None], Field(description='Query Google Maps from a particular region or country. For a list of supported region/country codes see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes (Alpha-2 code). Default: us')] = None,
                     language: Annotated[Union[str, None], Field(description='Set the language of the results. For a list of supported language codes see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes . Default: en')] = None) -> dict: 
    '''Get all / paginate business reviews by Business Id.'''
    url = 'https://local-business-data.p.rapidapi.com/business-reviews'
    headers = {'x-rapidapi-host': 'local-business-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'business_id': business_id,
        'limit': limit,
        'offset': offset,
        'translate_reviews': translate_reviews,
        'query': query,
        'sort_by': sort_by,
        'fields': fields,
        'region': region,
        'language': language,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def business_review_details(business_id: Annotated[str, Field(description='The Business Id of the business for which the review belongs. Accepts google_id / business_id or place_id. Examples: 0x880fd393d427a591:0x8cba02d713a995ed ChIJkaUn1JPTD4gR7ZWpE9cCuow')],
                            review_author_id: Annotated[str, Field(description='Review author id (i.e review author_id field). In addition, batching of up to 20 Review Author Ids is supported in a single request using a comma separated list (e.g. review_author_id=id1,id2).')],
                            region: Annotated[Union[str, None], Field(description='Query Google Maps from a particular region or country. For a list of supported region/country codes see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes (Alpha-2 code). Default: us')] = None,
                            language: Annotated[Union[str, None], Field(description='Set the language of the results. For a list of supported language codes see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes . Default: en')] = None) -> dict: 
    '''Get the details of a specific review by Google Id / Business Id or Google Place Id and Review Author Id.'''
    url = 'https://local-business-data.p.rapidapi.com/review-details'
    headers = {'x-rapidapi-host': 'local-business-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'business_id': business_id,
        'review_author_id': review_author_id,
        'region': region,
        'language': language,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def business_photos(business_id: Annotated[str, Field(description='Unique Business Id. Accepts google_id / business_id or place_id. Examples: 0x880fd393d427a591:0x8cba02d713a995ed ChIJkaUn1JPTD4gR7ZWpE9cCuow')],
                    limit: Annotated[Union[int, float, None], Field(description='Maximum number of business photos to return. Default: 20 Allowed values: 1-100 Default: 20')] = None,
                    cursor: Annotated[Union[str, None], Field(description='Specify the cursor obtained from the previous request to get the next of result page (use for pagination).')] = None,
                    is_video: Annotated[Union[bool, None], Field(description='Only return video type media (type=video) or not. Default: false')] = None,
                    region: Annotated[Union[str, None], Field(description='Query Google Maps from a particular region or country. For a list of supported region/country codes see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes (Alpha-2 code). Default: us')] = None,
                    fields: Annotated[Union[str, None], Field(description='A comma separated list of review fields to include in the response (field projection). By default all fields are returned. Example: type,photo_url')] = None) -> dict: 
    '''Get business photos by Business Id.'''
    url = 'https://local-business-data.p.rapidapi.com/business-photos'
    headers = {'x-rapidapi-host': 'local-business-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'business_id': business_id,
        'limit': limit,
        'cursor': cursor,
        'is_video': is_video,
        'region': region,
        'fields': fields,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def business_photo_details(business_id: Annotated[str, Field(description='The Business Id of the business for which the photo belongs. Accepts google_id / business_id or place_id. Examples: 0x880fd393d427a591:0x8cba02d713a995ed ChIJkaUn1JPTD4gR7ZWpE9cCuow')],
                           photo_id: Annotated[str, Field(description='Photo Id of the photo to fetch. In addition, batching of up to 20 Photo Ids is supported in a single request using a comma separated list (e.g. photo_id=id1,id2).')]) -> dict: 
    '''Get extra details about a business photo - caption, owner name and avatar, and more information. Supports batching of up to 20 Photo Ids.'''
    url = 'https://local-business-data.p.rapidapi.com/photo-details'
    headers = {'x-rapidapi-host': 'local-business-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'business_id': business_id,
        'photo_id': photo_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def business_posts(business_id: Annotated[str, Field(description='Unique Business Id. Accepts google_id / business_id or place_id. Examples: 0x880fd393d427a591:0x8cba02d713a995ed ChIJkaUn1JPTD4gR7ZWpE9cCuow')],
                   cursor: Annotated[Union[str, None], Field(description='Specify the cursor obtained from the previous request to get the next of result page (use for pagination).')] = None,
                   region: Annotated[Union[str, None], Field(description='Query Google Maps from a particular region or country. For a list of supported region/country codes see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes (Alpha-2 code). Default: us')] = None,
                   language: Annotated[Union[str, None], Field(description='Set the language of the results. For a list of supported language codes see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes . Default: en')] = None) -> dict: 
    '''Get all / paginate Business Owner Posts ("From the owner" section on Google Maps) by Business Id, sorted chronologically.'''
    url = 'https://local-business-data.p.rapidapi.com/business-posts'
    headers = {'x-rapidapi-host': 'local-business-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'business_id': business_id,
        'cursor': cursor,
        'region': region,
        'language': language,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def reverse_geocoding(lat: Annotated[Union[int, float], Field(description='Default: 40.6958453')],
                      lng: Annotated[Union[int, float], Field(description='Default: -73.9799119')],
                      region: Annotated[Union[str, None], Field(description='Query Google Maps from a particular region or country. For a list of supported region/country codes see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes (Alpha-2 code). Default: us')] = None,
                      language: Annotated[Union[str, None], Field(description='Set the language of the results. For a list of supported language codes see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes . Default: en')] = None,
                      fields: Annotated[Union[str, None], Field(description='A comma separated list of business fields to include in the response (field projection). By default all fields are returned. Example: business_id,type,phone_number,full_address')] = None) -> dict: 
    '''Get the details of a place or address in a specific geographic location by latitude and longitude (reverse geocoding). This endpoint implements the "What's here?" functionality available on Google Maps (right click on the map).'''
    url = 'https://local-business-data.p.rapidapi.com/reverse-geocoding'
    headers = {'x-rapidapi-host': 'local-business-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'lat': lat,
        'lng': lng,
        'region': region,
        'language': language,
        'fields': fields,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def bulk_search(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Search local businesses on Google Maps. Batching of up to 20 queries is supported in a single request.'''
    url = 'https://local-business-data.p.rapidapi.com/search'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'local-business-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def autocomplete(query: Annotated[str, Field(description='Search query')],
                 region: Annotated[Union[str, None], Field(description='Return results biased to a particular region. For a list of supported region/country codes see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes (Alpha-2 code). Default: us')] = None,
                 language: Annotated[Union[str, None], Field(description='Set the language of the results. For a list of supported language codes see https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2 . Default: en')] = None,
                 coordinates: Annotated[Union[str, None], Field(description='Geographic coordinates of the location from which the query is applied - recommended to use so that results are biased towards this location. Defaults to some central location in the region (see the region parameter).')] = None) -> dict: 
    '''Returns place/address, business and query predictions for text-based geographic queries.'''
    url = 'https://local-business-data.p.rapidapi.com/autocomplete'
    headers = {'x-rapidapi-host': 'local-business-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'region': region,
        'language': language,
        'coordinates': coordinates,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
