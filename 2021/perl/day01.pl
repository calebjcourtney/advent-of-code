#!/usr/bin/perl

# inspired by a friend's work, who did part 1
# modified to include part 2, though there's not much different

use strict;

# part 1
open(my $hInput, '<', '../inputs/input01.txt');
my $iIncreases = 0;
my @aLines = <$hInput>;
foreach my $i(0 .. $#aLines-1){
        chomp(my $iPrevious = @aLines[$i]);
        chomp(my $iLine2 = @aLines[$i+1]);
        $iIncreases++ if($iLine2 > $iPrevious);
}

print $iIncreases . "\n";


# part 2
open(my $hInput, '<', '../inputs/input01.txt');
my $iIncreases = 0;
my @aLines = <$hInput>;
foreach my $i(0 .. $#aLines-3){
        chomp(my $iPrevious = @aLines[$i]);
        chomp(my $iLine4 = @aLines[$i+3]);
        $iIncreases++ if($iLine4 > $iPrevious);
}


print $iIncreases;
