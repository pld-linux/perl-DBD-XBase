%include	/usr/lib/rpm/macros.perl
Summary:	DBD-XBase perl module
Summary(pl):	Modu³ perla DBD-XBase
Name:		perl-DBD-XBase
Version:	0.173
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/DBD/DBD-XBase-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-DBI
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBD-XBase perl module.

%description -l pl
Modu³ perla DBD-XBase.

%prep
%setup -q -n DBD-XBase-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README ToDo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz eg
%attr(755,root,root) %{_bindir}/dbfdump
%{perl_sitelib}/DBD/XBase.pm
%{perl_sitelib}/XBase.pm
%{perl_sitelib}/XBase
%{_mandir}/man[13]/*
