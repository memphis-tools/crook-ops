const { test, expect } = require('@playwright/test');

test('index page renders without Spring or JS errors', async ({ page }) => {
  const errors = [];
  page.on('pageerror', e => errors.push(e));
  page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });

  const resp = await page.goto('/');
  expect(resp.status()).toBe(200);
  expect(errors).toHaveLength(0);
  await expect(page.locator('body')).not.toBeEmpty();
});
