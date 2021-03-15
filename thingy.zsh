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

local menu=($abilities level bonus help quit)

local skills_active=''
local skills_passive='' # wtf are these?

# derived goodies
local total_points=0
local spent_points=0
local available_points=0

help() {
  echo "HA! As if."
}

read "name?Name? "
read "level?Level? "
read "bonus_points?BONUS? as if you deserve one "
echo "Original, level one scores:"
if true; then
for ability in $abilities; do
  read "$ability?$ability: "
done
fi
read "skills_active?Fucking active skills: "
read "skills_passive?Fucking passive skills: "

dump_state () {
  for var in name level $abilities; do
    echo "-> $var: ${(P)var}"
  done
}

points_from_level() {
  local level=$1
  echo $(( (level*level + level )/2 + level - 2))
}
total_points=$(points_from_level $level)
: $(( total_points+=bonus_points ))
echo "POINTS!!!!! $total_points"

level_cost() {
  current_level=$1
  echo $(( $current_level/10 + 1))
}

loop=true
while $loop; do
  echo "==> MENU: $menu"
  available_points=$(( total_points - spent_points ))
  dump_state
  echo "You have $available_points to spend. Spend wisely"
  read "ability?Select: "
  case $ability in
    (q|Q|quit|e|Q|exit) loop=false ; continue ;;
    help) help ;;
    level)
      echo "Level up!";
      : $(( level++ )) ;
      total_points=$(( $(points_from_level $level) + bonus_points ));
      ;;
    bonus)
      echo "You have $bonus_points currently."
      read "bonus_points?New value: "
      total_points=$(( $(points_from_level $level) + bonus_points ));
      ;;
  esac
  (( ${abilities[(I)$ability]} )) || continue
  read "direction?Up or Down? "
  case $direction in
    d*|D*) cost=$(level_cost $(( ${(P)ability} - 1 )) ); net=earn;;
    u*|U*) cost=$(level_cost ${(P)ability}); net=cost ;;
  esac
  print "That will $net you $cost points."
  read "verify?Are you sure? "
  case $verify in
    y*|Y*|sure|whatever) ;;
    *) echo "Your loss."; continue ;;
  esac
  case $net in
    cost)
      (( cost > available_points )) && { print "Nice try, dipshit"; continue ; }
      : $(( $ability++ ))
      : $(( spent_points+=cost ))
      ;;
    earn)
      : $(( $ability-- ))
      : $(( spent_points-=cost ))
      ;;
  esac
done
