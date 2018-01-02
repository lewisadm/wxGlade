#!/usr/bin/perl -w -- 
#
# generated by wxGlade
#
# To get wxPerl visit http://www.wxperl.it
#

use Wx qw[:allclasses];
use strict;

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade

package Frame194;

use Wx qw[:everything];
use base qw(Wx::Frame);
use strict;

use Wx::Locale gettext => '_T';
sub new {
    my( $self, $parent, $id, $title, $pos, $size, $style, $name ) = @_;
    $parent = undef              unless defined $parent;
    $id     = -1                 unless defined $id;
    $title  = ""                 unless defined $title;
    $pos    = wxDefaultPosition  unless defined $pos;
    $size   = wxDefaultSize      unless defined $size;
    $name   = ""                 unless defined $name;

    # begin wxGlade: Frame194::new
    $self = $self->SUPER::new( $parent, $id, $title, $pos, $size, $style, $name );
    $self->SetSize(Wx::Size->new(800, 600));
    $self->{list_box_single} = Wx::ListBox->new($self, wxID_ANY, wxDefaultPosition, wxDefaultSize, [_T("Listbox wxLB_SINGLE")], wxLB_SINGLE);
    $self->{list_box_multiple} = Wx::ListBox->new($self, wxID_ANY, wxDefaultPosition, wxDefaultSize, [_T("Listbox wxLB_MULTIPLE")], wxLB_MULTIPLE);
    $self->{list_box_extended} = Wx::ListBox->new($self, wxID_ANY, wxDefaultPosition, wxDefaultSize, [_T("Listbox wxLB_EXTENDED")], wxLB_EXTENDED);
    $self->{check_list_box_single} = Wx::CheckListBox->new($self, wxID_ANY, wxDefaultPosition, wxDefaultSize, [_T("CheckListBox wxLB_SINGLE")], , wxDefaultPosition, wxDefaultSize, wxLB_SINGLE);
    $self->{check_list_box_multiple} = Wx::CheckListBox->new($self, wxID_ANY, wxDefaultPosition, wxDefaultSize, [_T("CheckListBox wxLB_MULTIPLE")], , wxDefaultPosition, wxDefaultSize, wxLB_MULTIPLE);
    $self->{check_list_box_extended} = Wx::CheckListBox->new($self, wxID_ANY, wxDefaultPosition, wxDefaultSize, [_T("CheckListBox wxLB_EXTENDED")], , wxDefaultPosition, wxDefaultSize, wxLB_EXTENDED);

    $self->__set_properties();
    $self->__do_layout();

    # end wxGlade
    return $self;

}


sub __set_properties {
    my $self = shift;
    # begin wxGlade: Frame194::__set_properties
    $self->SetTitle(_T("frame_1"));
    $self->{list_box_single}->SetSelection(0);
    $self->{list_box_multiple}->SetSelection(0);
    $self->{list_box_extended}->SetSelection(0);
    $self->{check_list_box_single}->SetSelection(0);
    $self->{check_list_box_multiple}->SetSelection(0);
    $self->{check_list_box_extended}->SetSelection(0);
    # end wxGlade
}

sub __do_layout {
    my $self = shift;
    # begin wxGlade: Frame194::__do_layout
    $self->{sizer_1} = Wx::GridSizer->new(2, 3, 0, 0);
    $self->{sizer_1}->Add($self->{list_box_single}, 1, wxALL|wxEXPAND, 5);
    $self->{sizer_1}->Add($self->{list_box_multiple}, 1, wxALL|wxEXPAND, 5);
    $self->{sizer_1}->Add($self->{list_box_extended}, 1, wxALL|wxEXPAND, 5);
    $self->{sizer_1}->Add($self->{check_list_box_single}, 1, wxALL|wxEXPAND, 5);
    $self->{sizer_1}->Add($self->{check_list_box_multiple}, 1, wxALL|wxEXPAND, 5);
    $self->{sizer_1}->Add($self->{check_list_box_extended}, 1, wxALL|wxEXPAND, 5);
    $self->SetSizer($self->{sizer_1});
    $self->Layout();
    # end wxGlade
}

# end of class Frame194

1;

package MyApp;

use base qw(Wx::App);
use strict;

sub OnInit {
    my( $self ) = shift;

    Wx::InitAllImageHandlers();

    my $Bug194_Frame = Frame194->new();

    $self->SetTopWindow($Bug194_Frame);
    $Bug194_Frame->Show(1);

    return 1;
}
# end of class MyApp

package main;

unless(caller){
    my $local = Wx::Locale->new("English", "en", "en"); # replace with ??
    $local->AddCatalog("app"); # replace with the appropriate catalog name

    my $app = MyApp->new();
    $app->MainLoop();
}
