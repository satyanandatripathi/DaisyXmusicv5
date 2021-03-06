# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import os
from DaisyXMusic.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL
class Messages():
      START_MSG = "**βπ π₯πππ£π [{}](tg://user?id={})!**\n\nπ€ππͺ βπππ ππ€ βπππ¦π£π ππ  ππ₯π€π¦π€π¦ππ πππ π'π π₯ππ πΈππ§ππππ πππππ π₯πππππ ππ¦ππ₯πππ¦πππ₯ππ πππ ππ π₯ ππ¦π£π£πππ₯ππͺ πͺπ π¦ ππ£π ππ₯ π€π₯ππ£π₯ π€π₯π£πππ π π ππͺ π§π πππ ππππ₯ ππ π₯ π€ππ£π§πππ"
      HELP_MSG = [
        ".",
f"""
**βππͺ π₯πππ£π πππππ ππ ππππ π₯π  {PROJECT_NAME}

βͺοΈ {PROJECT_NAME} βππ π‘πππͺ ππ¦π€ππ ππ πͺπ π¦π£ ππ£π π¦π‘'π€ π§π πππ ππππ₯ ππ€ π¨πππ ππ€ πππππππ'π€

βͺοΈ πΈπ€π€ππ€π₯πππ₯ ππππ >> @{ASSISTANT_NAME}\n\nβππππ πππ©π₯ ππ π£ πππ€π₯π£π¦ππ₯ππ ππ€**
""",

f"""
πππ₯π₯πππ π¦π‘

π) ππππ ππ π₯ πππππ (πΎπ£π π¦π‘ πππ ππ πππππππ ππ π¦π€π ππ‘πππͺ)
π) ππ₯ππ£π₯ π π§π πππ ππππ₯
π) ππ£πͺ `/play [π€π ππ ππππ]` ππ π£ π₯ππ πππ£π€π₯ π₯πππ ππͺ ππ πππππ
*) ππ π¦π€ππ£ππ π₯ ππ ππππ ππππ πͺ ππ¦π€ππ, ππ ππ π₯ πππ @{ASSISTANT_NAME} π₯π  πͺπ π¦π£ ππ£π π¦π‘ πππ π£ππ₯π£πͺ

π½π π£ βππππππ ππ¦π€ππ βπππͺ
π) ππππ ππ πππππ π π πͺπ π¦π£ πππππππ 
π) ππππ /userbotjoinchannel ππ ππππππ ππ£π π¦π‘
π) βπ π¨ π€πππ ππ ππππππ€ ππ ππππππ ππ£π π¦π‘

**=>> ππ ππ βπππͺπππ π§**

- /play : βπππͺ π₯ππ π£ππ’π¦ππ€π₯π π€π ππ
- /play [πͺπ₯ π¦π£π] : βπππͺ π₯ππ πππ§ππ πͺπ₯ π¦π£π
- /play [π£ππ‘ππͺ πͺπ  ππ¦πππ ]: βπππͺ π£ππ‘ππππ ππ¦πππ 
- /dplay : βπππͺ π€π ππ π§ππ ππππ«ππ£
- /splay : βπππͺ π€π ππ π§ππ πππ  π€πππ§π
- /ytplay : π»ππ£πππ₯ππͺ π‘πππͺ π€π ππ π§ππ ππ π¦π₯π¦ππ ππ¦π€ππ

**=>> βπππͺππππ β―**

- /player : ππ‘ππ πππ₯π₯ππππ€ ππππ¦ π π π‘πππͺππ£
- /skip : ππππ‘π€ π₯ππ ππ¦π£π£πππ₯ π₯π£πππ
- /pause : βππ¦π€π π₯π£πππ
- /resume : βππ€π¦πππ€ π₯ππ π‘ππ¦π€ππ π₯π£πππ
- /end : ππ₯π π‘π€ πππππ π‘πππͺππππ
- /current : πππ π¨π€ π₯ππ ππ¦π£π£πππ₯ βπππͺπππ π₯π£πππ
- /playlist : πππ π¨π€ π‘πππͺπππ€π₯

*βπππͺππ£ πππ πππ πππ π π₯πππ£ ππππ€ ππ©πππ‘π₯ /play, /current  πππ /playlist  ππ£π π πππͺ ππ π£ ππππππ€ π π π₯ππ ππ£π π¦π‘.
""",
        
f"""
**=>> βππππππ ππ¦π€ππ βπππͺ π **

βͺοΈ π½π π£ ππππππ ππ£π π¦π‘ ππππππ€ π πππͺ:

- /cplay [π€π ππ ππππ] - π‘πππͺ π€π ππ πͺπ π¦ π£ππ’π¦ππ€π₯ππ
- /cdplay [π€π ππ ππππ] - π‘πππͺ π€π ππ πͺπ π¦ π£ππ’π¦ππ€π₯ππ π§ππ ππππ«ππ£
- /csplay [π€π ππ ππππ] - π‘πππͺ π€π ππ πͺπ π¦ π£ππ’π¦ππ€π₯ππ π§ππ πππ  π€πππ§π
- /cplaylist - πππ π¨ ππ π¨ π‘πππͺπππ πππ€π₯
- /cccurrent - πππ π¨ ππ π¨ π‘πππͺπππ
- /cplayer - π π‘ππ ππ¦π€ππ π‘πππͺππ£ π€ππ₯π₯ππππ€ π‘ππππ
- /cpause - π‘ππ¦π€π π€π ππ π‘πππͺ
- /cresume - π£ππ€π¦ππ π€π ππ π‘πππͺ
- /cskip - π‘πππͺ πππ©π₯ π€π ππ
- /cend - π€π₯π π‘ ππ¦π€ππ π‘πππͺ
- /userbotjoinchannel - πππ§ππ₯π ππ€π€ππ€π₯πππ₯ π₯π  πͺπ π¦π£ ππππ₯

πππππππ ππ€ πππ€π  πππ ππ π¦π€ππ πππ€π₯πππ π π π ( /cplay = /channelplay )

βͺοΈ ππ πͺπ π¦ ππ πππ₯ ππππ π₯π  π‘πππͺ ππ ππππππ ππ£π π¦π‘:

π) πΎππ₯ πͺπ π¦π£ πππππππ ππ».
π) βπ£πππ₯π π ππ£π π¦π‘ π¨ππ₯π π₯ππ₯π₯ππ: βππππππ ππ¦π€ππ: πͺπ π¦π£_πππππππ_ππ
π) πΈππ ππ π₯ ππ€ βππππππ πππππ π¨ππ₯π ππ¦ππ π‘ππ£ππ€
π) πΈππ @{ASSISTANT_NAME} π₯π  π₯ππ πππππππ ππ€ ππ πππππ.
π) ππππ‘ππͺ π€πππ ππ ππππππ€ ππ πͺπ π¦π£ ππ£π π¦π‘.
""",

f"""
**=>> ππ π£π π₯π π ππ€ π§βπ§**

- /ππ¦π€πππ‘πππͺππ£ [π π/π ππ]: πΌπππππ/π»ππ€ππππ ππ¦π€ππ π‘πππͺππ£
- /ππππππππππ: ππ‘πππ₯ππ€ πππππ ππππ  π π πͺπ π¦π£ ππ£π π¦π‘. ππ£πͺ ππ ππ π₯ ππ€π'π₯ π£πππ ππππ«π πππππ
- /π¦π€ππ£ππ π₯ππ ππ: πππ§ππ₯π @{πΈππππππΈβπ_βπΈππΌ} ππ€ππ£ππ π₯ π₯π  πͺπ π¦π£ ππππ₯

**=>> βπ ππππππ€ ππ π£ ππ¦ππ  ππ€ππ£π€ βοΈ**

 - /π¦π€ππ£ππ π₯ππππ§ππππ - π£πππ π§π ππ€π€ππ€π₯πππ₯ ππ£π π πππ ππππ₯π€
 - /ππππ€π₯ <π£ππ‘ππͺ π₯π  πππ€π€πππ> - πππ πππππͺ ππ£π ππππ€π₯ π£ππ‘ππππ πππ€π€πππ π₯π  πππ ππππ₯π€
 - /pmpermit [on/off] - ππππππ/πππ€ππππ π‘ππ‘ππ£πππ₯ πππ€π€πππ
*ππ¦ππ  ππ€ππ£π€ πππ ππ©πππ¦π₯π πππͺ ππ πππππ ππ πππͺ ππ£π π¦π‘π€

"""
      ]
