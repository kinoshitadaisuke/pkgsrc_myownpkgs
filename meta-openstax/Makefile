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
DEPENDS+=	openstax-computer-python>=0:../../pkgsrc_myownpkgs/openstax-computer-python
DEPENDS+=	openstax-science-astronomy>=0:../../pkgsrc_myownpkgs/openstax-science-astronomy
DEPENDS+=	openstax-science-chemistry>=0:../../pkgsrc_myownpkgs/openstax-science-chemistry
DEPENDS+=	openstax-science-physics>=0:../../pkgsrc_myownpkgs/openstax-science-physics
DEPENDS+=	openstax-math-algebra>=0:../../pkgsrc_myownpkgs/openstax-math-algebra
DEPENDS+=	openstax-math-calculus>=0:../../pkgsrc_myownpkgs/openstax-math-calculus
DEPENDS+=	openstax-math-statistics>=0:../../pkgsrc_myownpkgs/openstax-math-statistics

.include "../../mk/bsd.pkg.mk"
