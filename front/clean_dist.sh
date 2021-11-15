echo "vendor.xxxxx.js -> vendor.js"
mv dist/assets/vendor* dist/assets/vendor.js
echo "updating linking..."
cat dist/index.html | sed -E 's/\/vendor.*\.js/\/vendor\.js/g' > dist/ed.html
mv dist/ed.html dist/index.html
echo "Done."
