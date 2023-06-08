# $NetBSD$

DISTNAME=	typeshed_client-2.3.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=t/typeshed_client/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/JelleZijlstra/typeshed_client
COMMENT=	A library for accessing stubs in typeshed
LICENSE=	mit

PYTHON_VERSIONS_INCOMPATIBLE=	27

DEPENDS+=	${PYPKGPREFIX}-importlib-resources>=1.4.0:../../devel/py-importlib-resources
DEPENDS+=	${PYPKGPREFIX}-setuptools>=42:../../devel/py-setuptools
DEPENDS+=	${PYPKGPREFIX}-wheel>0:../../devel/py-wheel

USE_LANGUAGES=	# none

.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
