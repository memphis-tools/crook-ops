module.exports = {
  use: { baseURL: 'http://localhost:8080' },
  webServer: {
    command: 'sh -c "java -jar $(ls target/*.war | head -1)"',
    url: 'http://localhost:8080/index.html',
    reuseExistingServer: true,
    timeout: 120_000,
  },
  testDir: './tests',
};
