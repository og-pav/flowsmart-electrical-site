#!/bin/bash
# One-off: recover Anthony's original job photos from the Wayback Machine
# after the old WordPress host went away at DNS cutover.
cd "$(dirname "$0")" || exit 1
mkdir -p assets/img/remote
B="https://web.archive.org/web/2023id_/https://flowsmartelec.com.au/wp-content/uploads/2023/05"
get () { curl -sS -L --max-time 30 -A "Mozilla/5.0" -o "assets/img/remote/$2" "$B/$1"; }
get misc-862342412-480w.jpg          fse_kitchen.jpg
get misc-722215405-480w.jpg          fse_sparky.jpg
get misc-556416247-480w.jpg          fse_commercial.jpg
get misc-900217718-320w.jpg          fse_switch.jpg
get IMG_1861-640w.jpg                kaiser_1.jpg
get IMG_1864-480w.jpg                kaiser_2.jpg
get IMG_1856-e1683691260556.jpg      vogue_1.jpg
get IMG_1855.jpg                     vogue_2.jpg
get IMG_1848-e1683691266133.jpg      vogue_3.jpg
get IMG_1850.jpg                     vogue_4.jpg
get IMG_1851-e1683691273313.jpg      vogue_5.jpg
get IMG_1852.jpg                     vogue_6.jpg
get IMG_1854-e1683691281340.jpg      vogue_7.jpg
get IMG_1847.jpg                     vogue_8.jpg
echo "JPEGs recovered: $(file assets/img/remote/*.jpg 2>/dev/null | grep -c JPEG)"
du -sh assets/img/remote
