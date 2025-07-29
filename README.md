markdown
# Local Business Data MCP Server

## Overview

The Local Business Data MCP Server provides fast, reliable, and comprehensive access to local business and Point of Interest (POI) information. This server allows users to access the most up-to-date business data in real-time, sourced from leading platforms. The server is designed for seamless integration into various applications and projects, offering rich data insights to boost functionality and user experience.

## Key Features

- **Extensive Data Access**: Retrieve detailed business and POI information including address, website, phone, email, ratings, reviews, and more.
- **Real-Time Updates**: Access data that is updated in real-time, ensuring the information is always current and accurate.
- **Comprehensive Search Capabilities**: Utilize multiple search functions including default search, nearby search, and search within specific areas.
- **Category Support**: Supports over 4000 business categories, providing detailed and specific search results.
- **Custom Services**: Offers tailored services for specific needs, such as fetching data for all businesses within a certain category in a specific region.

## Getting Started

To begin using the Local Business Data MCP Server, follow these steps:

1. **Choose a Subscription Plan**: Select a plan that suits your needs and subscribe to gain access to the server's tools.
2. **Implement the Tools**: Integrate the server's tools into your application or workflow using the provided documentation and code snippets.
3. **Make Your First Query**: Use the search functionalities to retrieve local business data and incorporate it into your projects.

## Authentication

Authentication is handled via specific headers that must be included with each request. Ensure you have your unique key set up correctly to access the server's functionalities.

## Response Structure

All responses from the server include a status, a request ID, and relevant data or error information. The structure is designed to be intuitive and easy to parse, facilitating smooth integration.

## Tools and Functionalities

### Search Tools

- **Search**: Search for local businesses with options to retrieve emails and social profile links.
- **Search In Area**: Target businesses in a specific geographic area defined by coordinates and zoom level.
- **Search Nearby**: Find businesses near specific geographic coordinates.

### Business Details

- **Business Details**: Access full business details, including contact information and social profiles.
- **Business Reviews**: Retrieve and paginate through business reviews.

### Additional Features

- **Business Photos**: Obtain business photos with pagination support.
- **Reverse Geocoding**: Get place details by latitude and longitude.
- **Autocomplete**: Get predictions for place, address, and business queries.

## Rate Limiting

Each subscription plan includes specific rate limits to manage the number of requests per time period. Ensure your usage aligns with your plan to avoid hitting these limits.

## Error Handling

The server uses HTTP status codes to indicate errors. Common errors include malformed requests, invalid keys, and rate limit breaches. Implement error handling in your application to manage these responses gracefully.

## Support

For further assistance, custom plans, or specific queries, please contact our support team. We are here to help you make the most out of the Local Business Data MCP Server.

---

This README provides a succinct overview of the Local Business Data MCP Server, highlighting its functionalities and how to effectively integrate it into your applications for enhanced data access and user engagement.