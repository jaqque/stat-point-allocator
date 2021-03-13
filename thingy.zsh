#!/usr/bin/env zsh

local name=''
local level=0
local abilities=(str end agi int cha lck)
local str=0
local end=0
local agi=0
local int=0
local cha=0
local lck=0
local bonus_points=0

local skills_active=''
local skills_passive='' # wtf are these?

# derived goodies
local total_points=0
local spent_points=0
local available_points=0

read "name?Name? "
read "level?Level? "
read "bonus_points?BONUS? as if you deserve one "
if false; then
for ability in $abilities; do
  read "$ability?$ability "
done
fi

str=45
dump_state () {
  for var in name level $abilities; do
    echo "$var: ${(P)var}"
  done
}

points_from_level() {
  local level=$1
  echo $(( (level*level + level )/2 + level - 2))
}
total_points=$(points_from_level $level)
: $(( total_points+=bonus_points ))
dump_state; echo "POINTS!!!!! $total_points"

level_cost() {
  current_level=$1
  echo $(( $current_level/10 + 1))
}
loop=true

echo "$abilities"
while $loop; do
  available_points=$(( total_points - spent_points ))
  dump_state
  echo "You have $available_points to spend. Spend wisely"
  read "ability?What to upgrade? (quit to quit) "
  case $ability in
    (q|quit|e|exit) loop=false ; continue ;;
  esac
  (( ${abilities[(I)$ability]} )) || continue
  cost=$(level_cost ${(P)ability})
  print "That will cost you $cost points."
  read "verify?Are you sure? "
  case $verify in
    y|Y|yes|Yes|YES|sure|whatever) ;;
    *) echo "Your loss."; continue ;;
  esac
  (( cost > available_points )) && { print "Nice try, dipshit"; continue ; }
  : $(( $ability++ ))
  : $(( spent_points+=cost ))
done
