#!/usr/bin/lua

session:setVariable("continue_on_fail","USER_BUSY,NO_ANSWER,TIMEOUT,NO_USER_RESPONSE")
--get the dial extension number
exten = session:getVariable("destination_number")
exten_len=string.len(exten)

--test the dial length
if (exten_len == 4) then
--freeswitch.consoleLog("NOTICE","the dialpled numbers is:"..exten.."\n")

--Connect the local MySQL database(DBname,User,Password)
--local dbh = freeswitch.Dbh("test","fs","123qwe")

--Connect the ODBC DSN Database(odbcsourcename:Username:Passwod),in odbc.ini
local dbh = freeswitch.Dbh("odbc://fs:fs:123qwe")

freeswitch.consoleLog("NOTICE","start connect DB...\r\n")

assert(dbh:connected())

--Get the SIP User's Dial string

dbh:query("select url from registrations where reg_user="..exten,function(row)
        freeswitch.consoleLog("NOTICE","------------------------------------------")
        freeswitch.consoleLog("NOTICE",string.format("%s\n",row.url))
        freeswitch.consoleLog("NOTICE","------------------------------------------")
        exten_url = string.format("%s",row.url)
end);

--If the user not registration,answer the call,and tell the user call net called

if (exten_url == nil) then
  session:answer()
  session:sleep(2000)
  session:streamFile("/usr/local/freeswitch/sounds/en/us/callie/ivr/ivr-call_cannot_be_completed_as_dialed.wav")
  session:streamFile("/usr/local/freeswitch/sounds/en/us/callie/ivr/ivr-please_check_number_try_again.wav")
  session:sleep(2000)
  session:hangup()
  

else

---define the split string function,to get the dial string
function Split(szFullString, szSeparator)  
local nFindStartIndex = 1  
local nSplitIndex = 1  
local nSplitArray = {}  
while true do  
   local nFindLastIndex = string.find(szFullString, szSeparator, nFindStartIndex)  
   if not nFindLastIndex then  
    nSplitArray[nSplitIndex] = string.sub(szFullString, nFindStartIndex, string.len(szFullString))  
    break  
   end  
   nSplitArray[nSplitIndex] = string.sub(szFullString, nFindStartIndex, nFindLastIndex - 1)  
   nFindStartIndex = nFindLastIndex + string.len(szSeparator)  
   nSplitIndex = nSplitIndex + 1  
end  
return nSplitArray  
end  

local list = Split(exten_url,";")

local str_url = list[1]

--freeswitch.consoleLog("NOTICE","########################################################the strl_url is: "..str_url.."\n")

--Bridge the SIP User

session:execute("bridge",str_url)

--If bridge Failed,Tell the cause
obSession = freeswitch.Session(str_url)

local cause = obSession:hangupCause()

--freeswitch.consoleLog("INFO","########################################################the cause is:"..cause.."\n")
if  (cause == "USER_BUSY") then 
session:setVariable("call_time_out","10")
session:sleep(2000)
session:answer()
--freeswitch.consoleLog("INFO","########################################################the cause is:"..cause.."\n")
--Now play the file tell the user is busy now
session:streamFile("/usr/local/freeswitch/sounds/en/us/callie/ivr/8000/ivr-user_busy.wav")
session:hangup()
session:hangup()
session:hangup()

--If the use reject the call,tell the dial's user
elseif (cause == "NO_USER_RESPONSE") then
session:setVariable("call_time_out","10")
session:answer()
session:streamFile("/usr/local/freeswitch/sounds/en/us/callie/ivr/8000/ivr-terribly_wrong_awkward.wav")
session:hangup()
session:hangup()

else
freeswitch.consoleLog("INFO","######################################################################\n")

end

--This hangup when the bridge scueefull
session:hangup()




end


--if the dial length is not 4 ,tell check the number
else
  session:answer()
  session:setVariable("call_time_out","20")
  session:sleep(2000)
  session:streamFile("/usr/local/freeswitch/sounds/en/us/callie/ivr/ivr-call_cannot_be_completed_as_dialed.wav")
  session:streamFile("/usr/local/freeswitch/sounds/en/us/callie/ivr/ivr-please_check_number_try_again.wav")
  session:sleep(2000)
  session:hangup()
end

