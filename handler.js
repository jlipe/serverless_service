'use strict';

const AWS = require('aws-sdk');

const docClient = new AWS.DynamoDB.DocumentClient();


module.exports.hello = async (event) => {
  return {
    statusCode: 200,
    body: JSON.stringify(
      {
        message: 'Go Serverless v1.0! Your function executed successfully!',
        input: event,
      },
      null,
      2
    ),
  };

  // Use this code if you don't use the http event with the LAMBDA-PROXY integration
  // return { message: 'Go Serverless v1.0! Your function executed successfully!', event };
};

module.exports.getHeadlines = async (event) => {
  const queryString = event.queryStringParameters
  const sources = queryString["sources"] || "NY Times"
  const sourceArray = sources.split(",")

  const payload = []

  for (const source of sourceArray) {
    // By default this will query the most recent 1000 headlines
    const params = {
      TableName: "361_headlines",
      IndexName: "SourceTime",
      KeyConditionExpression: "#source = :source",
      ScanIndexForward: false,
      ExpressionAttributeNames: {
        "#source": "source"
      },
      ExpressionAttributeValues: {
        ":source": source
      }
    }
    const results = await docClient.query(params).promise()
    payload.push(...results.Items)
  }

  return {
    statusCode: 200,
    body: JSON.stringify(
      {
        items: payload
      }
    )
  }
}

module.exports.generateQuiz = async (event) => {
  const queryString = event.queryStringParameters
  const sources = queryString["sources"] || "NY Times"
  const sourceArray = sources.split(",")
  const limit = queryString["limit"]

  const payload = []

  for (const source of sourceArray) {
    // By default this will query the most recent 1000 headlines
    const params = {
      TableName: "361_headlines",
      IndexName: "SourceTime",
      KeyConditionExpression: "#source = :source",
      ScanIndexForward: false,
      ExpressionAttributeNames: {
        "#source": "source"
      },
      ExpressionAttributeValues: {
        ":source": source
      }
    }
    const results = await docClient.query(params).promise()
    
    // Choosing a random set of elements from array
    const selected = []
    const chosenIndexes = new Set()
    let randN
    while (selected.length < limit) {
      randN = Math.floor(Math.random() * results.Items.length)
      if (chosenIndexes.has(randN)) {
        continue
      } else {
        selected.push(results.Items[randN])
        chosenIndexes.add(randN)
      }
    }
    payload.push(...selected)
  }

  return {
    statusCode: 200,
    body: JSON.stringify(
      {
        items: payload.sort((a, b) => 0.5 - Math.random()) // Returning in a random order
      }
    )
  }
}
