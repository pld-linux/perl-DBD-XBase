#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBD
%define	pnam	XBase
Summary:	XBase - Reading and writing the DBF files from Perl
Summary(pl):	XBase - Czytanie i zapisywanie plików DBF z poziomu Perla
Name:		perl-DBD-XBase
Version:	0.220
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-DBI
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module can read and write XBase database files, known as dbf in
dBase and FoxPro world. It also reads memo fields from the dbt and
fpt files, if needed. An alpha code of reading index support for ndx,
ntx, mdx, idx and cdx is available for testing -- see the DBD::Index(3)
man page. Module XBase provides simple native interface to XBase files.
For DBI compliant database access, see the DBD::XBase and DBI modules
and their man pages.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README ToDo
%attr(755,root,root) %{_bindir}/dbfdump
%{perl_sitelib}/DBD/XBase.pm
%{perl_sitelib}/XBase.pm
%{perl_sitelib}/XBase
%{_mandir}/man[13]/*
%{_examplesdir}/%{name}-%{version}
