#! /usr/bin/perl
use warnings;
use strict;
use Cwd;
use Spreadsheet::ParseExcel;


my $parser   = Spreadsheet::ParseExcel->new();
my $workbook = $parser->parse('1.xls');

if ( !defined $workbook ) {
    die $parser->error(), ".\n";
}
print "$workbook";
    for my $worksheet ( $workbook->worksheets() ) {
print "$worksheet\n";
        my ( $row_min, $row_max ) = $worksheet->row_range();
        my ( $col_min, $col_max ) = $worksheet->col_range();

        for my $row ( $row_min .. $row_max ) {
            for my $col ( $col_min .. $col_max ) {

                my $cell = $worksheet->get_cell( $row, $col );
                next unless $cell;

                print "Row, Col    = ($row, $col)\n";
                print "Value       = ", $cell->value(),       "\n";
                print "Unformatted = ", $cell->unformatted(), "\n";
                print "\n";
            }
        }
    }