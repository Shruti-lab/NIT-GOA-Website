/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './public/**/*.{html,js}',
    "./node_modules/flowbite/**/*.js",
  ],
  theme: {
    extend: {},
  },
  variants: {
    display: ['responsive', 'group-hover', 'group-focus'],
   },
  plugins: [
    require('flowbite/plugin')
  ],
}