# $NetBSD$

DISTNAME=	check_manifest-0.51
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=c/check_manifest/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/mgedmin/check-manifest
COMMENT=	Check MANIFEST.in in a Python source package for completeness
LICENSE=	mit

DEPENDS+=	${PYPKGPREFIX}-build>=0.1:../../devel/py-build
DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools

USE_LANGUAGES=	# none

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
