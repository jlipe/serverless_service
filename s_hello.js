
var serverlessSDK = require('./serverless_sdk/index.js');
serverlessSDK = new serverlessSDK({
  orgId: 'jlippy',
  applicationName: 'headlineservice',
  appUid: 'w1VMj9cCCNJ6XrbN7g',
  orgUid: '44056344-8e1c-418c-b334-ba5fa4002204',
  deploymentUid: 'f2ab18af-9368-4401-b22e-a115f5dc807d',
  serviceName: 'headlineservice',
  shouldLogMeta: true,
  shouldCompressLogs: true,
  disableAwsSpans: false,
  disableHttpSpans: false,
  stageName: 'dev',
  serverlessPlatformStage: 'prod',
  devModeEnabled: false,
  accessKey: null,
  pluginVersion: '5.5.3',
  disableFrameworksInstrumentation: false
});

const handlerWrapperArgs = { functionName: 'headlineservice-dev-hello', timeout: 6 };

try {
  const userHandler = require('./handler.js');
  module.exports.handler = serverlessSDK.handler(userHandler.hello, handlerWrapperArgs);
} catch (error) {
  module.exports.handler = serverlessSDK.handler(() => { throw error }, handlerWrapperArgs);
}