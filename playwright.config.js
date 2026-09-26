module.exports = {
  use: { baseURL: 'http://localhost:8080' },
  webServer: {
    command: 'sh -c "java -jar $(ls target/*.war | head -1)"',
    url: 'http://localhost:8080/index.html',
    reuseExistingServer: false,
    timeout: 120_000,
    stdout: 'print',   // ← add: shows Spring's console output in the test log
  },
  testDir: './tests',
};
