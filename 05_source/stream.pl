
print "Content-type: text/html\n\n";


my @into_the_stream = qw( 1 2 3 );
my $stepsound = "..step";

print "You step into the stream ..";

foreach my $step (@into_the_stream) {
	
	print "<H".$step.">".$stepsound."</H".$step.">";
	
	if($step == 3) {
		sleep 1;
		print "<br>But the water has moved on";
		sleep 1;
		print "<br>Sorry, this page is not here";
	
	}
	
	
}


