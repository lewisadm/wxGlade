#!/usr/bin/perl -w --
#
# generated by wxGlade "faked test version"
#
# To get wxPerl visit http://wxPerl.sourceforge.net/
#

# This is an automatically generated file.
# Manual changes will be overwritten without warning!

use Wx 0.15 qw[:allclasses];
use strict;
package MyStartApp;

use base qw(Wx::App);
use strict;

use MyAppFrame;

sub OnInit {
    my( $self ) = shift;

    Wx::InitAllImageHandlers();

    my $appframe = MyAppFrame->new();

    $self->SetTopWindow($appframe);
    $appframe->Show(1);

    return 1;
}
# end of class MyStartApp

package main;

unless(caller){
    my $myapp = MyStartApp->new();
    $myapp->MainLoop();
}