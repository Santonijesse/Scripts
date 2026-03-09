# App Status Summary

Device: ZY22HS5QFQ | Android 15

---

## Food & Delivery

| App | Status | APK in README | Notes |
|-----|--------|---------------|-------|
| DoorDash | y | com.dd.doordash | OK |
| McDonald's | y | com.mcdonalds.app | OK |
| Uber Eats | y | com.ubercab.eats | OK |
| Starbucks | y | com.starbucks.mobilecard | OK |
| Taco Bell | y | com.tacobell.ordering | OK |
| OpenTable | y | com.opentable | OK |
| Instacart | y | com.instacart.client | OK |
| Too Good To Go | y | com.app.tgtg | OK |
| Domino's | y | com.dominospizza | OK |
| Yelp | y | com.yelp.android | OK |
| Dunkin' | y | com.dunkinbrands.otgo | OK |
| ReciMe | y | com.recime.app | OK |
| Chick-fil-A | y | com.chickfila.cfaflagship | OK |
| Dutch Bros | y | com.dutchbros.loyalty | OK |
| Chipotle | y | com.chipotle.ordering | OK |
| Subway | y | com.subway.mobile.subwayapp03 | OK |
| Little Caesars | y | com.littlecaesars | OK |
| Wingstop | n | com.wingstop.mobile | Package looks correct. Error is likely appActivity — README has `com.wingstop.mobile.MainActivity`. Try removing the appActivity line entirely and let Appium resolve it. |
| Buffalo Wild Wings | n | com.buffalowildwings.ordering | Package uncertain. App may use `com.buffalowildwings.ecomm` or similar. Verify with: `adb shell pm list packages \| Select-String "buffalowild"` |
| Crumbl | n | com.crumbl.app | Package looks correct. Try `com.crumbl.app.ui.MainActivity` as the activity, or remove the activity line. |

---

## Maps, Navigation & Parking

| App | Status | APK in README | Notes |
|-----|--------|---------------|-------|
| Google Maps | y | com.google.android.apps.maps | OK |
| Waze | y | com.waze | OK |
| Organic Maps | n | com.organicmaps | Package correct. Correct activity is `app.organicmaps.MwmActivity` — update README. |
| ParkMobile | n | com.parkmobile.android | Package may be wrong. Possible correct package: `com.parkmobile.zone`. Verify on device. |
| Transit | y | com.thetransitapp.droid | OK |
| MapXplorer | n | com.mapxplorer.app | App may not exist on Google Play under this package. Cannot verify — check device with `adb shell pm list packages \| Select-String "mapxplorer"`. |
| SpotHero | y | com.spothero.spothero | OK |
| Shell Motorist | n | com.shell.sitibv.motorist | Package looks correct. No known activity — try removing appActivity line. |
| ParkWhiz | n | com.parkwhiz | Package may be wrong. Try `com.parkwhiz.android`. Verify on device. |
| Metropolis Parking | n | com.metropolis.parking | Package uncertain. Verify with: `adb shell pm list packages \| Select-String "metropolis"` |
| onX Hunt | n | com.onxmaps.hunt | Package correct. No appActivity set — Appium should auto-resolve but may fail. Try `com.onxmaps.hunt.ui.activity.SplashActivity`. |
| onX Offroad | n | com.onxmaps.offroad | Same issue as onX Hunt. |
| MTA TrainTime | n | com.mta.trait | TraIT = TRAIn Time, so package is likely correct. No activity set — try `com.mta.trait.activities.MainActivity`. |
| Neshan Maps | n | com.neshan.maps | Package looks correct. No activity set — try `ir.neshan.maps.activity.SplashActivity`. |
| ChargePoint | y | com.coulombtech | OK (listed in README as "Coulomb Tech") |
| Speedometer Simple | n? | com.speedometer.simple | Name may have changed or app removed. Check Play Store — current popular speedometer apps include `com.danogentili.speedometer` (Speedometer GPS). |
| Earnify | y | NOT IN README | Package unknown. Verify with `adb shell pm list packages \| Select-String "earnify"` and add to README. |
| Citymapper | y | com.citymapper.app.release | OK |
| Moovit | y | com.tranzmate | OK (listed in README as "TranzMate" — this is TranzMate which uses Moovit backend) |
| AMap Global | n | com.autonavi.minimap | This is the China-domestic Amap package. The global version may not be available on Google Play or uses a different package. |

---

## Social & News

| App | Status | APK in README | Notes |
|-----|--------|---------------|-------|
| X (Twitter) | y | com.twitter.android | OK |
| Substack | y | com.substack.app | OK |
| Reddit | y | com.reddit.frontpage | OK |
| CrimeRadar | n | com.crimeradar.app | Package uncertain. Verify on device. App may have been removed or rebranded. |
| Nextdoor | y | com.nextdoor | OK |
| NewsBreak | y | com.particlenews.newsbreak | OK |
| New York Times | y | com.nytimes.android | OK |
| Citizen | n | com.spotcrime.android | **WRONG PACKAGE** — `com.spotcrime.android` is SpotCrime, not Citizen. Citizen's correct package is `com.sp0n.citizen`. Update README. |
| Police Scanner Radio & Fire | n? | com.police.scanner.radio | App name or package may have changed. Verify on device. |
| TrueShort | n? | com.trueshort.app | App may have been renamed or removed from Play Store. Verify on device. |
| Ground News | y | NOT IN README | Package not in README. Likely `com.groundnews.android`. Add to README. |
| Fizz | n? | com.fizz.app | App may have been rebranded. Verify on device. |
| AP News | n | com.apnews | Package may be wrong. AP News actual package is `mnn.Android`. Try that instead. |
| Wall Street Journal | n | com.wsj.android | Package correct. No activity set — Appium may fail to auto-resolve. Try `com.wsj.android.LaunchActivity`. |
| The Pour Over | n? | com.thepourover.app | App may have changed name or been removed. Verify on device. |
| Podcasts | timeout | com.podcast.podcasts | Timed out (not an error crash). Package may be wrong or app was slow to launch. This package belongs to CastBox. Verify which podcast app is installed. |
| Clubhouse | y | com.clubhouse.app | OK |
| Police Scanner: Fire Radio | n? | com.bstore.android.policescanner | App may have changed. Verify on device. |
| Ring Neighbors | n | com.ring.neighbors | Package correct. No activity set — try `com.ring.neighbors.activities.MainActivity`. |
| Fox News | y | com.foxnews.android | OK |

---

## Other

| App | Status | APK in README | Notes |
|-----|--------|---------------|-------|
| Microsoft Copilot | y | com.microsoft.copilot | OK |
| ChatGPT | y | com.openai.chatgpt | OK |
| TikTok Lite | n | com.zhiliaoapp.musically.go | Package correct. Error is likely activity — try removing appActivity or use `com.zhiliaoapp.musically.go.main.MainActivity`. |
| Temu | y | com.einnovation.temu | OK |
| TikTok | n | com.ss.android.ugc.trill | Package correct (international TikTok). Activity `com.ss.android.ugc.trill.splash.SplashActivity` should work — may need app reinstall or activity update. |
| Instagram | y | com.instagram.android | OK |
| WhatsApp | y | com.whatsapp | OK |
| Edge Aura | y | com.wallpaper.edge.aura | OK |
| FreeCash | y | com.freecash.app2 | OK |
| ReelShort | y | com.newleaf.app.android.victor | OK — Note: README labels this app as "Victor" but the correct current name is **ReelShort**. Update README heading. |
| Threads | y | com.instagram.barcelona | OK |
| DoorDash Driver | y | com.doordash.driverapp | OK |
| CapCut | y | com.lemon.lvoverseas | OK |
| SHEIN | y | com.zzkko | OK |
| Peacock | y | com.peacocktv.peacockandroid | OK |
| Tubi | y | com.tubitv | OK |
| PayPal | y | com.paypal.android.p2pmobile | OK |
| Cash App | y | com.squareup.cash | OK |
| Whatnot | y | com.whatnot_mobile | OK |
| Facebook | y | com.facebook.katana | OK |

---

## Summary of Action Items

- **Update README package**: Citizen → `com.sp0n.citizen` (currently set to SpotCrime `com.spotcrime.android`)
- **Update README package**: AP News → `mnn.Android` (currently `com.apnews`)
- **Update README heading**: "Victor" → ReelShort (package `com.newleaf.app.android.victor` is correct)
- **Add to README**: Ground News (`com.groundnews.android`), Earnify (package unknown — verify on device)
- **Verify on device** (may not be launchable): MapXplorer, Speedometer Simple, Fizz, TrueShort, Police Scanner Radio & Fire, Police Scanner Fire Radio, The Pour Over
- **Try activity fix**: Organic Maps (`app.organicmaps.MwmActivity`), Ring Neighbors, MTA TrainTime, onX Hunt/Offroad, WSJ
- **Verify package**: Buffalo Wild Wings, ParkMobile, ParkWhiz, Metropolis, CrimeRadar
