module.exports = {
  use: { baseURL: 'http://localhost:8080' },
  webServer: {
    command: 'sh -c "java -jar $(ls target/*.war | head -1)"',
    url: 'http://localhost:8080/',
    reuseExistingServer: false,
    timeout: 120_000,
    stdout: 'print',
  },
  testDir: './tests',
};
