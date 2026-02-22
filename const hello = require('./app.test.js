const hello = require('./app');
test('outputs the correct string', () => {
    expect(hello()).toBe("hello world");
});
