module.exports = {
  use: { baseURL: 'http://localhost:8080' },
  webServer: {
    command: 'java -jar target/*.jar',
    url: 'http://localhost:8080/index.html',
    reuseExistingServer: true,
    timeout: 120_000,
  },
  testDir: './tests',
};
