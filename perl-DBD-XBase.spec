%include	/usr/lib/rpm/macros.perl
Summary:	DBD-XBase perl module
Summary(pl):	Modu³ perla DBD-XBase
Name:		perl-DBD-XBase
Version:	0.160
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/DBD/DBD-XBase-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-DBI
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBD-XBase perl module.

%description -l pl
Modu³ perla DBD-XBase.

%prep
%setup -q -n DBD-XBase-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/XBase
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[13]/* \
        Changes README ToDo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README,ToDo}.gz eg
%attr(755,root,root) %{_bindir}/dbfdump

%{perl_sitelib}/DBD/XBase.pm
%{perl_sitelib}/XBase.pm
%{perl_sitelib}/XBase
%{perl_sitearch}/auto/XBase

%{_mandir}/man[13]/*
