# $NetBSD$

DISTNAME=	# empty
PKGNAME=	meta-openstax-1.0
PKGREVISION=	0
CATEGORIES=	meta-pkgs math science
MASTER_SITES=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
DISTFILES=	# empty

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
COMMENT=	Meta package for OpenStax textbooks
LICENSE=	cc-by-v4.0

META_PACKAGE=	yes

.include "../../mk/bsd.prefs.mk"

# textbooks
DEPENDS+=	openstax-science-astronomy>=0:../../pkgsrc_myownpkgs/openstax-science-astronomy
DEPENDS+=	openstax-science-university-physics>=0:../../pkgsrc_myownpkgs/openstax-science-university-physics

.include "../../mk/bsd.pkg.mk"
