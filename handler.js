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
  const source = queryString["source"] || "NY Times"
  console.log("Source", source)


  const params = {
    TableName: "361_headlines",
    KeyConditionExpression: "#source = :source",
    ExpressionAttributeNames: {
      "#source": "source"
    },
    ExpressionAttributeValues: {
      ":source": source
    }
  }

  const results = await docClient.query(params).promise()
  console.log(results)

  return {
    statusCode: 200,
    body: JSON.stringify(
      {
        items: results.Items
      }
    )
  }
}
