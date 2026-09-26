const { test, expect } = require('@playwright/test');

test('index.html renders without Spring or JS errors', async ({ page }) => {
  const errors = [];
  page.on('pageerror', e => errors.push(e));      // JS exceptions
  page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });

  const resp = await page.goto('/index.html');      // uses baseURL
  expect(resp.status()).toBe(200);                  // catches Spring 500
  expect(errors).toHaveLength(0);                   // catches broken JS
  // optional: assert real content, not just status
  await expect(page.locator('body')).not.toBeEmpty();
});
